# define arguments
output_dir = 'output-small'
model_type = 'gpt2'
model_name_or_path = 'microsoft/DialoGPT-small'
config_name = 'microsoft/DialoGPT-small'
tokenizer_name = 'microsoft/DialoGPT-small'
cache_dir = 'cached' # folder para guardar el modelo tokenizer y configuracion
block_size = 512
do_train = True
do_eval = True
evaluate_during_training = False
train_batch_size = 4
per_gpu_eval_batch_size = 4
learning_rate = 5e-5
weight_decay = 0.0
adam_epsilon = 1e-8
max_grad_norm = 1.0
num_train_epochs = 3
warmup_steps = 0 # usinf for scheduling learning rate
logging_steps = 1000
save_steps = 3500
save_total_limit = None
eval_all_checkpoints = False
no_cuda = False
should_continue = False # resume train from checkpoint
seed = 42

## special tokens
bos_token= '<|beginningoftext|>'
eos_token= '<|endoftext|>'
sep_token= '<|sep|>'
pad_token= '<|pad|>'
unk_token= '<|unk|>'

bot_token= '<|bot|>'
user_token= '<|user|>'