# kivy-led
## What is about ?
A led widget for kivy with default shapes. run __init__.py to see an example running. default shapes of led are provided (round, square, rounded square with or without line)

## properties
### state
'on' or 'off' whether the led is on or off
### led_type
three possible values :
- 'color' : changes the color when state changes (default colors try to match kivy default theme). colors can be set by the color_off and color_on properties (these are list properties in the style of [red,green,blue,opacity]). you must set the source property with a greyscale image. the widget will color this image with color_off or color_on.

- 'source' : set source_off and source_on properties and the image will change according to state.

- 'both' : source AND color will change according to state. so, you must set color_on, color_off, source_on and source_off.

### color_on
the image color when the state is on (when led_type equals to color or both). it's a list of the style [r,g,b,opacity]
### color_off
the image color when the state is off (when led_type equals to color or both). it's a list of the style [r,g,b,opacity]
### source_on
image source when the state is on.
### source_off
image source when the state is off
### auto_off
when set to True, the led goes automatically off after a short time. Useful to monitor network or serial connection.
### auto_off_delay
time to wait before automatically change state to off (in seconds)
