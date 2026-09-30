# DenClick Media

Archive of all existing tutorial and promo variations, raw captures, images, narration audio, intermediate edits, and final exports. All files were copied without removing the originals. Binary assets are tracked with Git LFS.

## Latest exports

- [Latest energetic promo — 107 seconds](client/promo-energy/DenClick-Energetic-107s-v2.mp4)
- [Earlier 107-second promo](client/promo-energy/DenClick-Energetic-107s.mp4)
- [95-second promo](client/promo-energy/DenClick-Energetic-95s.mp4)
- [Tutorial files and all variations](client/tutorial-output/)
- [Original promo versions](client/promo-output/)
- [Story promo versions](client/promo-story/)
- [Energetic promo versions and raw captures](client/promo-energy/)

## Download the complete archive

Install Git LFS before cloning:

```sh
git lfs install
git clone https://github.com/KinlieVenice/DenClick-Media.git
cd DenClick-Media
git lfs pull
```

Preserve the `client/` layout when restoring assets into the application workspace. The included production scripts are a snapshot; the maintained application source commit is `82af824` on `fix/appointment-time-and-printing`.

`media-manifest.json` lists every archived production file with its size and SHA-256 checksum. Future exports should use distinct version names rather than overwrite the only copy. Capture files use fictional demo data. Asset provenance is retained in the production folders.
