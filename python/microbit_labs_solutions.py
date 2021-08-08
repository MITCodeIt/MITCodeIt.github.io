# all of the sample solutions to the micro:bit minilabs for CodeIt 2
from microbit import *

def clapping_lights():
    lightsOn = False

    while True:
        if microphone.was_event(SoundEvent.LOUD):
            lightsOn = not lightsOn
            if lightsOn:
                display.show(Image('99999:'
                                   '99999:'
                                   '99999:'
                                   '99999:'
                                   '99999'))
            else:
                display.clear()
        sleep(100)

def name_tag():
    while True:
        display.scroll('Shelly')
        display.show(Image.HEART)
        sleep(2000)
        display.clear()

def flashing_emotions():
    while True:
        if button_a.is_pressed():
            for x in range(4):
                display.show(Image.HAPPY)
                sleep(200)
                display.clear()
                sleep(200)
        if button_b.is_pressed():
            for x in range(4):
                display.show(Image.SAD)
                sleep(200)
                display.clear()
                sleep(200)

def step_counter():
    steps = 0

    while True:
        if accelerometer.was_gesture('shake'):
            steps += 1
            display.show(steps)

def stopwatch():
    time = 0
    start = 0
    running = False

    while True:
        if running:
            display.show(Image.HEART)
            sleep(300)
            display.show(Image.HEART_SMALL)
            sleep(300)
        else:
            display.show(Image.ASLEEP)
        if pin_logo.is_touched():
            if running:
                time += running_time() - start
                running = False
                display.scroll(str(time / 1000))
            else:
                running = True
                start = running_time()

def temperature():
    currentTemp = temperature()
    max = currentTemp
    min = currentTemp

    while True:
        display.show('.')
        currentTemp = temperature()
        if currentTemp < min:
            min = currentTemp
        if currentTemp > max:
            max = currentTemp
        if button_a.was_pressed():
            display.scroll(min)
        if button_b.was_pressed():
            display.scroll(max)
        sleep(1000)
        display.clear()
        sleep(1000)

def nightlight():
    while True:
        if display.read_light_level() < 100:
            display.show(Image(
                "99999:"
                "99999:"
                "99999:"
                "99999:"
                "99999"))
        else:
            display.clear()
        sleep(2000)

def compass():
    compass.calibrate()

    while True:
        bearing = compass.heading()
        if bearing =< 45 or bearing > 315:
            display.show('N')
        elif bearing > 45 and bearing =< 135:
            display.show('E')
        elif bearing > 135 and bearing =< 225:
            display.show('S')
        elif bearing > 225 and bearing =< 315:
            display.show('W')
        else:
            display.show(' ')

def soundometer():
    # set of images for simple bar chart
    graph5 = Image("99999:"
                   "99999:"
                   "99999:"
                   "99999:"
                   "99999")

    graph4 = Image("00000:"
                   "99999:"
                   "99999:"
                   "99999:"
                   "99999")

    graph3 = Image("00000:"
                   "00000:"
                   "99999:"
                   "99999:"
                   "99999")

    graph2 = Image("00000:"
                   "00000:"
                   "00000:"
                   "99999:"
                   "99999")

    graph1 = Image("00000:"
                   "00000:"
                   "00000:"
                   "00000:"
                   "99999")

    graph0 = Image("00000:"
                   "00000:"
                   "00000:"
                   "00000:"
                   "00000")

    allGraphs = [graph0, graph1, graph2, graph3, graph4, graph5]

    # ignore first sound level reading
    soundLevel = microphone.sound_level()
    sleep(200)

    while True:
        # map sound levels from range 0-255 to range 0-5 for choosing graph image
        soundLevel = microphone.sound_level()

        # scale sound level
        fromRange = 255 - 0
        toRange = 5 - 0
        valueScaled = float(soundLevel - 0) / float(fromRange)
        newSoundLevel = int(0 + (valueScaled * toRange))
        display.show(allGraphs[newSoundLevel])

def metronome():
    import music
    tempo = 100

    while True:
        music.set_tempo(bpm=tempo)
        music.play(['C4:1', 'r:3'])  # play C for 1 tick, rest for 3 ticks
        if button_a.was_pressed():
            tempo -= 5
        if button_b.was_pressed():
            tempo += 5

def pet():
    import audio

    timer = 0
    display.show(Image(
        "00000:"
        "09090:"
        "00000:"
        "09990:"
        "00000"))
    audio.play(Sound.HELLO)

    while True:
        if pin_logo.is_touched():
            timer = 0
            display.show(Image.HAPPY)
            audio.play(Sound.HAPPY)
        elif accelerometer.was_gesture('shake'):
            timer = 0
            display.show(Image.SURPRISED)
            audio.play(Sound.GIGGLE)
        else:
            sleep(500)
            timer += 0.5
            # sleep for half a second only to make it react more quickly to logo touch & shake

        if timer == 20:
            display.show(Image.SAD)
            audio.play(Sound.SAD)
        elif timer == 30:
            display.show(Image.ASLEEP)
            audio.play(Sound.YAWN)
        elif timer == 40:
            display.show(Image.SKULL)
            audio.play(Sound.MYSTERIOUS)
            break