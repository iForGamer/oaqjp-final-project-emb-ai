import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        re1 = emotion_detector("I Am Glad This Happend")
        self.assertEqual(re1["dominant_emotion"],"joy")
        re2 = emotion_detector("I Am Really Mad About This")
        self.assertEqual(re2["dominant_emotion"],"anger")
        re3 = emotion_detector("I Feel Disgusted just Hearing about this")
        self.assertEqual(re3["dominant_emotion"],"disgust")
        re4 = emotion_detector("I Am So Sad About This")
        self.assertEqual(re4["dominant_emotion"],"sadness")
        re5 = emotion_detector("I Am Really Afraid that this will happen")
        self.assertEqual(re5["dominant_emotion"],"fear")

unittest.main()