from microbit import *
import radio
shipIsUp = True;

radio.on()

while True:
    if accelerometer.was_gesture("shake"):
        if (shipIsUp):
            display.show(Image.ARROW_S)
            print('lower_ship')
        else:
            display.show(Image.ARROW_N)
            print('raise_ship')
        shipIsUp = not shipIsUp
        # radio.send('toggle_space_ship_position')
        # sleep(50) # these sleeps after send are necessary to prevent message being continuously dispatched. no idea why
    elif button_a.is_pressed():
        display.show(Image.ARROW_E)
        radio.send('show_next_word')
        str = 'next_word:bob|previous_word_spelt_correctly:true'
        strParts = str.split('|');
        print(strParts);
        sleep(50);
    sleep(50)
