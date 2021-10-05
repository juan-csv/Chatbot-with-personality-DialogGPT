from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import config as cfg
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

def transform_dataset_to_features(list_context, tokenizer, Number_max_sentences = 3):
    """
    input: [context_1, context_2, ... context_N]
    output: context_1 <|sep|> context_2 '<|sep|>' ... '<|sep|>' context_N
    """
    

    flatten = lambda l: [item for sublist in l for item in sublist]

    if type(list_context) == str:
        list_context = [list_context]

    # reduce the length of context
    if len(list_context)>Number_max_sentences:
        list_context = list_context[-Number_max_sentences:]


    # transform sentences to tokens
    token_features = []
    for i,x in enumerate(list_context):
        tokens = tokenizer.encode(x) + [tokenizer.eos_token_id]
        token_features.append(tokens)
    
    # flat list
    token_features = flatten(token_features)

    return token_features


class Bot_rick():
    def __init__(self):
        cfg.output_dir = "Bot_Rick"
        self.tokenizer = AutoTokenizer.from_pretrained(cfg.output_dir)
        self.model = AutoModelForCausalLM.from_pretrained(cfg.output_dir)

    def get_response(self, history_chat):

        bot_input_ids = transform_dataset_to_features(history_chat, self.tokenizer)
        bot_input_ids = torch.unsqueeze(torch.Tensor(bot_input_ids),0)
        bot_input_ids = bot_input_ids.type(torch.int64)
        
        # generated a response while limiting the total chat history to 1000 tokens, 
        chat_history_ids = self.model.generate(
            bot_input_ids, 
            max_length=200,
            pad_token_id= self.tokenizer.pad_token_id,  
            no_repeat_ngram_size=3,       
            do_sample=True, 
            top_k=100, 
            top_p=0.7,
            temperature = 0.8
        )
        # pretty print last ouput tokens from bot
        res = self.tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        return res
#------------------------------------------------------------------------
if __name__ == '__main__':
    history_chat = ["Hello Rick"]
    
    my_bot = Bot_rick()
    res = my_bot.get_response(history_chat)
    print(res)

