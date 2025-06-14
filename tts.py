from fastapi import APIRouter, Query, Depends, FastAPI
from pydantic import BaseModel
from typing import Union, Optional
from enum import Enum
from enum import Enum
from typing import Union, Optional
from enum import Enum
from fastapi.responses import StreamingResponse, RedirectResponse
from tts import TTS

app = FastAPI()


class SplitMethod(str, Enum):
    # cut0 = "不切"
    # cut1 = "凑4句一切"
    # cut2 = "凑50字一切"
    # cut3 = "中文句号。切"
    # cut4 = "英文句号.切"
    # cut5 = "按标点符号切"
    cut0 = "cut0"
    cut1 = "cut1"
    cut2 = "cut2"
    cut3 = "cut3"
    cut4 = "cut4"
    cut5 = "cut5"


class TextLang(str, Enum):
    all_zh = "all_zh"
    en = "en"
    all_ja = "all_ja"
    zh = "zh"
    ja = "ja"
    all_yue = "all_yue"
    yue = "yue"
    ko = "ko"
    all_ko = "all_ko"
    auto = "auto"

class AudioFormat(str, Enum):
    WAV = "wav"
    OGG = "ogg"
    AAC = "aac"
    MP3 = "mp3"

class Params(BaseModel):
    text: Union[str, None] = Query(None, description="文本内容", title="文本内容")
    spk: Union[str, None] = Query(
        None, description="发音人,不设置走默认的。", title="发音人"
    )
    emotion: Union[str, None] = Query(
        None, description="情感,不设置走默认的", title="情感"
    )
    role: Optional[str] = Query(
        "", description="角色,不设置走默认的", title="角色"
    )
    engine: Optional[str] = Query("GPT-SoVITS", description="引擎名，默认是GPT-SoVITS", title="引擎")
    speed: float = Query(1.0, description="语速", title="语速")
    format: AudioFormat = Query(
        AudioFormat.WAV, description="输出文件格式", title="输出音频格式"
    )
    text_lang: TextLang = Query(TextLang.zh, description="文本语言", title="文本语言")
    split_bucket: bool = Query(False, description="是否启用分桶")
    batch_size: int = Query(10, description="分桶大小")
    batch_threshold: float = Query(0.5, description="分桶阈值")
    text_split_method: SplitMethod = Query(
        SplitMethod.cut0,
        description="文本切割方式.cut0(不切),cut1(凑4句一切),cut2(凑50字一切),cut3(中文句号。切),cut4(英文句号.切),cut5(按标点符号切)",
    )
    temperature: float = Query(0.5, description="temperature")
    top_k: int = Query(50, description="top_k")
    top_p: float = Query(0.9, description="top_p")
    ref_wav_path: Union[str, None] = Query(
        None, description="参考音频路径,优先使用参数的"
    )

    prompt_text: Union[str, None] = Query(None, description="参考文本，优先使用参数的")
    prompt_language: Union[str, None] = Query(
        None, description="参考语言，优先使用参数的"
    )
    return_fragment: bool = Query(False, description="分段返回，默认不启用")
    fragment_interval: float = Query(0.5, description="分段时间间隔")
    seed: int = Query(-1, description="随机种子，-1为不固定")
    stream: bool = Query(False, description="是否为流式语音")
    parallel_infer: bool = Query(False, description="是否启用并行推理")
    repetition_penalty: float = Query(1.0, description="重复惩罚")
    pitch: float = Query(1.0, description="音高")
    volume: float = Query(1.0, description="音量")
    duration: Union[float, None] = Query(None, description="固定时长")
    instruct_text: Union[str, None] = Query(None, description="指令文本,仅CosyVoice有效")


async def logic(params: Params):
    """TTS合成逻辑"""
    return b'\x00'

@app.post("/")
async def tts_post(params: Params):
    """TTS合成"""

    return StreamingResponse(
        logic(params),
        media_type=f"audio/{params.format.value}",
        headers={"Cache-Control": "no-cache"}
    )

@app.get("/")
async def tts_get(params: Params = Depends(Params)):
    """TTS合成"""
    return StreamingResponse(
        logic(params), 
        media_type=f"audio/{params.format.value}",
        headers={"Cache-Control": "no-cache"}
    )
    
@app.get("/config")
async def config():
    """获取配置"""
    return {"speaker": {
        "spk1": {
            "desc": "发音人简介描述",
            "emotion": {
                "情感1": {
                    "ref_wav_path": "参考音频路径",
                    "text": "参考文本",
                    "text_lang": "zh"
                },
                "情感2": {
                }
            }
        }
    }}


# 多音字部分
class MultiphonemeRequest(BaseModel):
    data: dict
    phoneme: dict

@app.post("/multiphoneme")
async def multiphoneme(params: MultiphonemeRequest):
    """多音字更新"""
    return {"message": "多音字更新成功"}
