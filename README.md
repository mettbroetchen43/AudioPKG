# AudioPKG - A ZIP based containerformat for Audiofiles including Metadata

## Introduction

You may already know file formats based on ZIP archives – like EPUB or ODT. These formats bundle content with metadata in a clean and extensible way.

**AudioPKG** follows the same principle: It’s a ZIP container that includes the audio file (e.g. `MP3` , ` FLAC` , ` OGG` ) and a `metadata.json` describing its metadata.

## Why AudioPKG?
Anyone who has ever written a tag editor, media organizer, or Telegram bot that parses metadata knows the pain:

    ID3 tags work differently than Vorbis comments.

    FLAC handles metadata differently than Opus.

    Each format has its own quirks, limitations, and corner cases.

**AudioPKG** solves this by separating metadata from the audio file entirely.
This makes metadata access predictable, editable, and format-agnostic.