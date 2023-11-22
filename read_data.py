import os
from random import choice
from audio_reader import load_wav
import matplotlib.pyplot as plt



pos_files = os.path.join("data", "Parsed_Capuchinbird_Clips")
neg_files = os.path.join("data", "Parsed_Not_Capuchinbird_Clips")


pos_sample = os.path.join(pos_files, choice(os.listdir(pos_files)))
neg_sample = os.path.join(neg_files, choice(os.listdir(neg_files)))


plt.plot(load_wav(pos_sample))
plt.plot(load_wav(neg_sample))
plt.show()