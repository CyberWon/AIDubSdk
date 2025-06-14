# 说明

本项目为AIDub/AI有声读物中的自定义引擎演示示例，并不包含完整的生成语音，需要自行开发。

为了丰富社区生态，并保证健康可长久的发展，部分优秀的项目，可选参与合作者计划(详见结尾)，帮助开发者实现盈利。

# 开发文档
示例用的是python+fastapi技术栈，相对来说开发很简单。AIDub只需要访问三个接口，自行实现逻辑即可。

## 配音接口
URL： `/`
HTTP方法：`GET/POST`
请求格式：JSON/Params
请求体: 
| 参数名 | 类型 | 默认值 | 描述 |
|--------|------|--------|------|
| text | string | null | 文本内容 |
| spk | string | null | 发音人,不设置走默认的 |
| emotion | string | null | 情感,不设置走默认的 |
| role | string | "" | 角色,不设置走默认的 |
| engine | string | "GPT-SoVITS" | 引擎名，默认是GPT-SoVITS |
| speed | float | 1.0 | 语速 |
| format | string | "wav" | 输出文件格式 |
| text_lang | string | "zh" | 文本语言 |
| split_bucket | boolean | false | 是否启用分桶 |
| batch_size | integer | 10 | 分桶大小 |
| batch_threshold | float | 0.5 | 分桶阈值 |
| text_split_method | string | "cut0" | 文本切割方式.cut0(不切),cut1(凑4句一切),cut2(凑50字一切),cut3(中文句号。切),cut4(英文句号.切),cut5(按标点符号切) |
| temperature | float | 0.5 | temperature |
| top_k | integer | 50 | top_k |
| top_p | float | 0.9 | top_p |
| ref_wav_path | string | null | 参考音频路径,优先使用参数的 |
| prompt_text | string | null | 参考文本，优先使用参数的 |
| prompt_language | string | null | 参考语言，优先使用参数的 |
| return_fragment | boolean | false | 分段返回，默认不启用 |
| fragment_interval | float | 0.5 | 分段时间间隔 |
| seed | integer | -1 | 随机种子，-1为不固定 |
| stream | boolean | false | 是否为流式语音 |
| parallel_infer | boolean | false | 是否启用并行推理 |
| repetition_penalty | float | 1.0 | 重复惩罚 |
| pitch | float | 1.0 | 音高 |
| volume | float | 1.0 | 音量 |
| duration | float | null | 固定时长 |
| instruct_text | string | null | 指令文本,仅CosyVoice有效 |
返回格式：数据流




## 获取发音人信息
URL：`/config`
HTTP方法：`GET`
返回格式：JSON
返回样例:
```json

{
    "speaker": {
        "spk1" : {
            "desc": "发音人简介描述",
            "emotion": {
                "情感1": {
                    "ref_wav_path":"参考音频路径", // 可选，
                    "text":"参考音频对应的参考文本", // 可选
                    "text_lang":"zh" // 可选，因为有可能是远程，填写了在本地端也读取不到这个文件。
                },
                "情感2": {
                   
                }
            }
        }
    }
}

```

## 设置多音字
URL: `/multiphoneme`
HTTP方法：`POST`
请求格式：JSON
请求体：{
   "data":{},
   "phoneme":{}, 
}
返回格式：JSON
返回样例: 
```
{"message": "多音字更新成功"}
```



# 合作者计划

1. 可在软件内的配音市场上架！超千名优质客户，只要你做的好用，就会有人买账。
2. 提供计费服务，可选按月、按年、永久买断。无需您额外准备服务器什么的，直接接入就可使用。
3. 当有客户有定制化服务时，可协作开发或独立开发，获取额外收益!
