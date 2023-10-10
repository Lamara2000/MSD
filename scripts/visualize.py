import matplotlib.pyplot as plt

def visualize_samples(images, labels, nb_samples):
    normal_samples = []
    pneumonia_samples = []

    i = 0
    while len(normal_samples) < nb_samples:
        if(labels[i] == 0) : normal_samples.append(images[i])
        i+=1   

    i = 0
    while len(pneumonia_samples) < nb_samples:
        if(labels[i] == 1) : pneumonia_samples.append(images[i])
        i+=1

    fig, axes = plt.subplots(nb_samples, 2, figsize=(10, 20))

    for i in range(nb_samples):
        axes[i][0].imshow(normal_samples[i])
        axes[i][0].set_title("NORMAL")
        axes[i][0].axis('off')
        axes[i][1].imshow(pneumonia_samples[i])
        axes[i][1].set_title("PNEUMONIA")
        axes[i][1].axis('off')

    plt.show() 