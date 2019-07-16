# Deep-Dance
#### Creating Dance using Deep Learning
 This project is fairly simple and the goal is to generate new dance videos by using various ML techniques. To be specific CNN, RNN and autoencoder is used in this project.

 - Dataset used : [video](https://www.youtube.com/watch?v=NdSqAAT28v0)

### Workflow of this project:
- Download the video ( I used 480p quality video )
- Extract 3 frames per second from the video using *ffmpeg* (this will result in **14401 frames**)
- Crop/Resize the frames to 800x480 for simplicity
- Clear the background of each frame or simply replace each pixel that is not black with white.(you'll understand why when you see the video)(use "*remove background.py*")
- Train the auto-encoder with new cleaned frames.The encoder output shape is (128).
- After training encode all images using **Encoder** that will result in new output of  shape **(14401,128)** in which all images are converted into its dense representation
- Train the **RNN** on new the 14401 sequence of 128 dims data.  
- After training predict new sequences from RNN 
- Convert new Sequence back into image using **Decoder**
- Stitch images into a video using *ffmpeg*
- Check out different results [here](https://github.com/akashraj9828/Deep-Dance/tree/master/video)

> Final Result

>![Result](https://github.com/akashraj9828/Deep-Dance/blob/master/result.gif?raw=true)
# Observation

Model| epoch | acc | loss | val_acc | val_loss |
|--|--|--|--|--|--|
|Autoencoder|27|0.964|0.007|0.964|0.007|
|RNN|853|0.800|0.048|0.799|0.049|

- Auto encoder accuracy

>![Autoencoder Accuracy](https://github.com/akashraj9828/Deep-Dance/blob/master/ai_dance_model/ai_dance_128_dims/aec/acc/graph_acc27.png?raw=true)

- Auto encoder loss
>![Autoencoder Accuracy](https://github.com/akashraj9828/Deep-Dance/blob/master/ai_dance_model/ai_dance_128_dims/aec/loss/graph_loss27.png?raw=true)


- RNN accuracy 
>	![RNN Accuracy](https://github.com/akashraj9828/Deep-Dance/blob/master/ai_dance_model/ai_dance_128_dims/rnn/acc/graph_acc.png?raw=true)
	
- RNN loss
>	![RNN Loss](https://github.com/akashraj9828/Deep-Dance/blob/master/ai_dance_model/ai_dance_128_dims/rnn/loss/graph_loss.png?raw=true)




# Result

> Dance generated Using Deep Learning

>![Result](https://github.com/akashraj9828/Deep-Dance/blob/master/result.gif?raw=true)


# Credits 
> Inspired by [carykh](https://github.com/carykh) 

> check out his video here : [video](https://www.youtube.com/watch?v=Sc7RiNgHHaE)
