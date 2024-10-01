#!/usr/bin/env bash

CUDA_VISIBLE_DEVICES=0,1,2,3 python finetune.py \
    --base_model '/storage_fast/vicuna/vicuna-7b/vicuna-7b-v1.5-16k' \
    --data_path '/storage_fast/vicuna/vicuna-7b/vicuna-7b-v1.5-16k/v1_ckpt' \
    --output_dir '/storage_fast/vicuna/vicuna-7b/vicuna-7b-v1.5-16k/v1' \
    --batch_size 4 \
    --micro_batch_size 1 \
    --num_epochs 2 \
    --learning_rate 1e-4 \
    --cutoff_len 1024 \
    --val_set_size 0 \
    --lora_r 8 \
    --lora_alpha 16 \
    --lora_dropout 0.05 \
    --lora_target_modules '[q_proj,v_proj]' \
    --train_on_inputs \
    --group_by_length

