## Bitmap loader 

Tested with 24bit-dept bitmaps as input. Place bitmap in bitmap-src, edit variables in bitmapLoader.py and run it.

Reccomended: restart display before running bitmapLoader.py

After the bitmap is uploaded to the display, you should see something like this output:

``

b'\r[cl] Bitmap sent into display. Display uart output:

b'\r[cl] Okay, proceeding to write bitmap.\n'

b'\r[cl] Okay, ready to parse bitmap #5, size 81x23 pixels.\n'

b'\r[cl] 3720 bytes left.\n'

b'\r[cl] 3348 bytes left.\n'

b'\r[cl] 2976 bytes left.\n'

b'\r[cl] 2604 bytes left.\n'

b'\r[cl] 2232 bytes left.\n'

b'\r[cl] 1860 bytes left.\n'

b'\r[cl] 1488 bytes left.\n'

b'\r[cl] 1116 bytes left.\n'

b'\r[cl] 744 bytes left.\n'

b'\r[cl] 372 bytes left.\n'

b'\rerase at 892928 \n'

b'\rMultipage write [3732]b@892928 \n'

b'\rerase at 819200 \n'

b'\rMultipage write [2052]b@819200 \n'

b'\r[cl] Bitmap #5 has been written.\n'
``

Note the last line - note this number down, you will use it later to refer to the bitmap you just uploaded.

If you're getting something wildly different (eg: lots of scrolling text, with no "Bitmap #5 has been written.\n'" at the end), restart display and try again.

If you're getting a message about running out of external memory, you can try wiping it. To do so, send "delete bitmaps\r" to display over uart. This will mark all bitmaps stored in memory for deletion (= delete the bitmap list and allow them to be overwritten).

Maximum bitmap size which can be drawn to display is limited (see objectVisualization.c for up-to-date info, at time of writing, maximum size is 128x128). If you need to draw something with higher resolution than that, save it as multiple bitmaps and draw them next to each other.



