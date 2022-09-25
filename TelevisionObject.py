class Television(object):
    def __init__(self,model, screen_size, volume, channel):
        self.model = model
        self.screen_size = screen_size
        self.__volume = volume
        self.__channel = channel
    print("A new television has been built")

sony = Television("Bravia", "60", "30", "1")
sony.model = "Bravia"
sony.screen_size ="60"
print("It is a Sony", sony.model, "with a", sony.screen_size, "inch screen size")

samsung = Television("KU6020", "65","30","1")
samsung.model = "KU6020"
samsung.screen_size = "60"
print("It is a Samsung", samsung.model, "model with", samsung.screen_size, "inch screen size")

@property
def volume(self):
    return self.__volume


@volume.setter
def volume(self, new_volume):
    new_volume = int(input("Input a volume"))
    if new_volume > 80:
        print("The volume is too loud")
    else:
        self.__volume = new_volume
        print("Volume set to", new_volume)

@property
def channel(self):
    return self.__channel

@channel.setter
def channel(self,new_channel):
    new_channel = int(input("Enter a new channel"))
    if new_channel > 50:
        print("Invalid channel number")
    else:
        self.__channel = new_channel
        print("Channel set to", new_channel)

print("Changing the volume of Sony")
new_volume = int(input("Enter a setting volume between 1 and 100: "))
if new_volume > 100:
    print('the volume is too big or too small')
else:
    print("The new volume is", new_volume)

print("Changing the channel of the Sony")
new_channel = int(input("Input a new channel between 1 and 100:"))
if new_channel > 100:
    print("That channel does not exist")
else:
    print("The new channel is", new_channel)










