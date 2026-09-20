"""Local WAV references for the TTS service's multipart synthesis API."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
MAX_REFERENCE_BYTES = 10 * 1024 * 1024


def resolve_voice_path(voice_path):
    """Resolve map/CLI paths relative to the project, independent of cwd."""
    path = Path(voice_path).expanduser()
    return (path if path.is_absolute() else PROJECT_ROOT / path).resolve()


def read_voice_file(voice_path):
    """Read a bounded RIFF/WAVE reference; the service validates WAV contents."""
    path = resolve_voice_path(voice_path)
    if path.suffix.lower() != ".wav":
        raise ValueError(f"Voice reference must be a local .wav path: {path}")
    with path.open("rb") as reference:
        content = reference.read(MAX_REFERENCE_BYTES + 1)
    if len(content) > MAX_REFERENCE_BYTES:
        raise ValueError(f"Voice reference exceeds the 10 MiB API limit: {path}")
    # Do not use Python 3.10's wave parser: it rejects WAVE_FORMAT_EXTENSIBLE,
    # which the service supports. Full decoding validation belongs to the API.
    if content[:4] != b"RIFF" or content[8:12] != b"WAVE":
        raise ValueError(f"Voice reference is not a RIFF/WAVE file: {path}")
    return path, content
