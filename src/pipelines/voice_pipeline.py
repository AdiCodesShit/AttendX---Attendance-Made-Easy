import io

import librosa
import numpy as np
import streamlit as st
import torch
import torch.nn.functional as F

from resemblyzer import VoiceEncoder, preprocess_wav


@st.cache_resource
def load_voice_encoder():
    return VoiceEncoder()


def load_audio(audio_bytes):
    """
    Loads audio and resamples to 16 kHz.
    Returns a numpy array.
    """
    audio, sr = librosa.load(
        io.BytesIO(audio_bytes),
        sr=16000,
        mono=True,
    )

    return preprocess_wav(audio)


def get_voice_embedding(audio_bytes):
    try:
        encoder = load_voice_encoder()

        wav = load_audio(audio_bytes)

        embedding = encoder.embed_utterance(wav)

        return embedding.tolist()

    except Exception as e:
        st.error(f"Voice Recognition Error:\n{e}")
        return None


def identify_speaker(new_embedding, candidates_dict, threshold=0.75):
    if new_embedding is None or len(candidates_dict) == 0:
        return None, 0.0

    new_embedding = torch.tensor(new_embedding, dtype=torch.float32)

    best_sid = None
    best_score = -1.0

    for sid, stored_embedding in candidates_dict.items():

        if stored_embedding is None:
            continue

        stored_embedding = torch.tensor(
            stored_embedding,
            dtype=torch.float32,
        )

        similarity = F.cosine_similarity(
            new_embedding.unsqueeze(0),
            stored_embedding.unsqueeze(0),
        ).item()

        if similarity > best_score:
            best_score = similarity
            best_sid = sid

    if best_score >= threshold:
        return best_sid, best_score

    return None, best_score


def process_bulk_audio(audio_bytes, candidates_dict, threshold=0.75):
    try:
        encoder = load_voice_encoder()

        wav = load_audio(audio_bytes)


        if len(wav) < 16000:
            return {}

        embedding = encoder.embed_utterance(wav).tolist()

        sid, score = identify_speaker(
            embedding,
            candidates_dict,
            threshold,
        )

        if sid is not None:
            return {sid: score}

        return {}

    except Exception as e:
        st.error(f"Bulk Audio Error:\n{e}")
        return {}