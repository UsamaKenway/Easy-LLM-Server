from load_llm import AutoGPTQForCausalLM, BaseQuantizeConfig
from transformers import pipeline, AutoTokenizer
from langchain.llms import HuggingFacePipeline
from transformers import StoppingCriteriaList
from LLMApp.utils.stop_sequence import StopOnTokens
import torch


class HFModel:
    def __init__(self, model_name: str) -> None:
        self.llm = None
        self.pipe = None
        self.base_model = None
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        stop_token_ids = self.tokenizer.convert_tokens_to_ids(['</s>'])
        self.stopping_criteria = StoppingCriteriaList([StopOnTokens(stop_token_ids)])

    def set_hf_pipe(self):
        self.pipe = pipeline(
            "text-generation",
            model=self.base_model,
            tokenizer=self.tokenizer,
            max_new_tokens=256,
            # max_length=256,
            temperature=0.6,
            top_p=0.95,
            # top_k=0,
            repetition_penalty=1.1,
            stopping_criteria=self.stopping_criteria,
        )
        self.llm = HuggingFacePipeline(pipeline=self.pipe)

    def load_model(self):
        self.base_model = AutoGPTQForCausalLM.from_quantized(self.model_name,
                                                             device="cuda:0",
                                                             use_safetensors=True)

        self.set_hf_pipe()
        return self.llm

    def unload_model(self):
        torch.cuda.empty_cache()


class GPTQModel(HFModel):
    def __init__(self, model_name: str):
        super().__init__(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

    def load_model(self):
        self.base_model = AutoGPTQForCausalLM.from_quantized(self.model_name,
                                                             device="cuda:0",
                                                             use_safetensors=True)
        self.set_hf_pipe()
        return self.llm




