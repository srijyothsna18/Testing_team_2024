from Base.Libraries.audacity import Audacity
from Base.Elements.Audacity_elements import Inputs
import pytest

IN = Inputs()
obj = Audacity()

@pytest.mark.audio
def test_open():
    obj.Lauch_App(IN.APP)
    result = obj.Open(IN.OPEN_FILE_NAME)
    assert result == True
    obj.close_App()

@pytest.mark.audio

def test_play():
    obj.Lauch_App(IN.APP)
    result = obj.Open(IN.OPEN_FILE_NAME)
    obj.play(IN.PLAY_TIME_IN_SEC)
    obj.close_App()

@pytest.mark.audio

def test_RMS():
    obj.Lauch_App(IN.APP)
    result = obj.Open(IN.OPEN_FILE_NAME)
    obj.Select_entire_audio()
    obj.Calculate_RMS(IN.FILE_TO_SAVE_RMS+r"/rms_value.png")
    obj.close_App()

@pytest.mark.audio

def test_Amplify():
    obj.Lauch_App(IN.APP)
    result = obj.Open(IN.OPEN_FILE_NAME)
    obj.Select_entire_audio()
    obj.Amplify(IN.AMPLIFY_VALUE)
    obj.close_App()

@pytest.mark.audio

def test_plot_spectrum():
    obj.Lauch_App(IN.APP)
    result = obj.Open(IN.OPEN_FILE_NAME)
    obj.plot(IN.FILE_PATH+r"\plotAnalysis.txt")
    obj.close_App()

@pytest.mark.audio

def test_generate_noise():
    obj.Lauch_App(IN.APP)
    obj.generate_noise()
    obj.close_App()

@pytest.mark.audio

def test_generate_silence():
    obj.Lauch_App(IN.APP)
    obj.generate_silence()
    obj.close_App()

@pytest.mark.audio

def test_select():
    obj.Lauch_App(IN.APP)
    result = obj.Open(IN.OPEN_FILE_NAME)
    obj.select(IN.START_TIME_TO_SELECT, IN.END_TIME_TO_SELECT)
    obj.noise_reduction()
    obj.close_App()

@pytest.mark.audio

def test_export_mp3():
    obj.Lauch_App(IN.APP)
    result = obj.Open(IN.OPEN_FILE_NAME)
    obj.export_as_mp3()
    obj.close_App()

@pytest.mark.audio

def test_export_wav():
    obj.Lauch_App(IN.APP)
    result = obj.Open(IN.OPEN_FILE_NAME)
    obj.export_as_wav()
    obj.close_App()

@pytest.mark.audio

def test_export_flac():
    obj.Lauch_App(IN.APP)
    result = obj.Open(IN.OPEN_FILE_NAME)
    obj.export_as_flac()
    obj.close_App()

@pytest.mark.audio

def test_save_as():
    obj.Lauch_App(IN.APP)
    result = obj.Open(IN.OPEN_FILE_NAME)
    obj.save_project_as(IN.SAVE_PROJECT)
    obj.close_App()
