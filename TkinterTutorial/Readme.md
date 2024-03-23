Tkinter
---------------

It is used for creating design for desktop application


Tkinter Widgets
----------------

It is a layout for individual element like button, textbox, textlabel etc

Geometry Manager
-----------------

There are 3 method for controlling the layout of application
1. `pack(options)` </br>
    options : fill, side, expand
2. `place(options)` </br>
    options : x, y, height, width, anchor, bordermode, relx, rely, relheight, relwidth
3. `grid(options)` </br>
    options : row, column, rowspan, columnspan, padx, pady, ipadx, ipady, sticky

Label Widget
------------------

`Label(root,options)` </br>
options : </br>

- `anchor` :	This option is mainly used for controlling the position of text in the provided widget size. The default value is CENTER which is used to align the text in center in the provided space. </br>
- `bd` :	This option is used for the border width of the widget. Its default value is 2 pixels. </br>
- `bitmap` :	This option is used to set the bitmap equals to the graphical object specified so that now the label can represent the graphics instead of text. </br>
- `bg` :	This option is used for the background color of the widget. </br>
- `cursor` :	This option is used to specify what type of cursor to show when the mouse is moved over the label. The default of this option is to use the standard cursor. </br>
- `fg` :	This option is used to specify the foreground color of the text that is written inside the widget. </br>
- `font` :	This option specifies the font type of text inside the label. </br>
- `height` :	This option indicates the height of the widget </br>
- `image` :	This option indicates the image that is shown as the label. </br>
- `justify` :	This option specifies the alignment of multiple lines in the label. The default value is CENTER. Other values are RIGHT, LEFT; you can justify according to your requirement </br>
- `padx` :	This option indicates the horizontal padding of the text. The default value of this option is 1. </br>
- `pady` :	This option indicates the vertical padding of the text. The default value of this option is 1. </br>
- `relief` :	This option indicates the type of border. The default value of this option is FLAT </br>
- `text` :	This option is set to the string variable and it may contain one or more than one line of text </br>
- `textvariable` :	This option is associated with a Tkinter variable that is (StringVar) with a label. If you change the value of this variable then text inside the label gets updated. </br>
- `underline` :	This option is used to underline a specific part of the text. The default value of this option =-1(no underline); you can set it to any integer value up to n and counting starts from 0. </br>
- `width` :	This option indicates the width of the widget. </br>
- `wraplength` :	Rather than having only one line as the label text, you can just break it to any number of lines where each line has the number of characters specified to this option </br>