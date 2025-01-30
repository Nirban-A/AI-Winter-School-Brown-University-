from langchain_ollama.llms import OllamaLLM
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama


def get_llm(model_name:str, 
            temp: float = 0.1,
            use_ollama:bool = True, 
            use_openai: bool = False,
            verbose: bool = True,
            ):
    try:
        if use_ollama:
            return OllamaLLM(model=model_name, 
                             temperature = temp, 
                             verbose= verbose)
        elif use_openai:
            return OpenAI(
                model=model_name,
                temperature=temp,
                max_retries=2,
                verbose = verbose,
            )
        else:
            raise Exception("Either use_ollama or use_openai must be true")

    except:
        raise Exception("Please enter a valid model name.")


def get_chat_llm(model_name:str, 
                use_ollama:bool = True, 
                use_openai: bool = False, 
                temp: float = 0.1,
                verbose: bool = True,
                ):
    try:
        if use_ollama:
            return ChatOllama(model=model_name, 
                             temperature = temp, 
                             verbose= verbose)
        elif use_openai:
            return ChatOpenAI(
                model=model_name,
                temperature=temp,
                max_retries=2,
                verbose = verbose,
            )
        else:
            raise Exception("Either use_ollama or use_openai must be true")

    except:
        raise Exception("Please enter a valid model name.")