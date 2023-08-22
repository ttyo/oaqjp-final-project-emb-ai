from emotion_detection import emotion_detector

def run_tests():
    test_cases = [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear")
    ]
    
    for text, expected_emotion in test_cases:
        result = emotion_detector(text)
        if expected_emotion in result:
            print(f"Test passed: '{text}' -> {expected_emotion}")
        else:
            print(f"Test failed: '{text}' -> {result}")

run_tests()
