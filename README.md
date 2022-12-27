# Ghadir AI microservice (v1.0)

Extract keyframes and voice on a video. Just use this request :

```python
curl --location --request POST 'http://localhost:8080/video' \
    --form 'file=@"./sample_video.mp4"' \
    --form 'duration="10"' \
    --form 'keyframes="5"'
```

Run the app :
```python
python app.py
```

Sample output:
```json
{
    "frames": [
        "http://localhost:8080/download?path=data/87485680-a9a4-4cb5-ab56-f3f1e461112a/video_4.jpeg",
        "http://localhost:8080/download?path=data/87485680-a9a4-4cb5-ab56-f3f1e461112a/video_0.jpeg",
        "http://localhost:8080/download?path=data/87485680-a9a4-4cb5-ab56-f3f1e461112a/video_3.jpeg",
        "http://localhost:8080/download?path=data/87485680-a9a4-4cb5-ab56-f3f1e461112a/video_1.jpeg",
        "http://localhost:8080/download?path=data/87485680-a9a4-4cb5-ab56-f3f1e461112a/video_2.jpeg"
    ],
    "id": "87485680-a9a4-4cb5-ab56-f3f1e461112a",
    "sound": "http://localhost:8080/download?path=data/87485680-a9a4-4cb5-ab56-f3f1e461112a/sound.wav"
}
```