- Running this command in CMD window
- input.mp4 is input video
- output.mp4 is output video
- logo.png is watermark exported from ppt
- running time is very long, but you can check the running progress by watching the   "frame=273364 fps= 65 q=-1.0 Lsize=  463582kB ***time=02:31:52.03*** bitrate= 416.8kbits/s dup=15 drop=2111 speed=2.18x"
- other best practices are here
> https://stackoverflow.com/questions/10918907/how-to-add-transparent-watermark-in-center-of-a-video-with-ffmpeg
> if you have multiple videos to process parallel, you can open multiple CMD windows.

ffmpeg -i input.mp4 -i logo.png -filter_complex "overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2" -codec:a copy output.mp4

## logo.png的生成技巧
- 打开PPT，插入文本框
- 设置文本框的长宽和实际视频的长宽成比例
- 设置文本框里面的字体大小
- 透明度设置
- save as png

## 加快效率的技巧
- 多开几个CMD窗口可以并行
