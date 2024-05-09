{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM6O+RsFYXqdVqCQLGgdqTg"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 51,
      "metadata": {
        "id": "haHZ1GabQrHu"
      },
      "outputs": [],
      "source": [
        "import tensorflow as tf\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import numpy as npy\n",
        "import os\n",
        "import io\n",
        "import pathlib\n",
        "import seaborn as sns\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "seed = 1\n",
        "tf.random.set_seed(seed)\n",
        "npy.random.seed(seed)"
      ],
      "metadata": {
        "id": "Ai3XHxVxyuYh"
      },
      "execution_count": 52,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "DATASET_PATH = r'C:\\Users\\Kristen\\Desktop\\DataSets\\TrainingFiles\\Manager1'\n",
        "data_dir = pathlib.Path(DATASET_PATH)\n",
        "if not data_dir.exists():\n",
        "  tf.keras.utils.get_file(\n",
        "      'Manager1',\n",
        "      origin = 'C:/Users/Kristen/Desktop/DataSets/TrainingFiles/Manager1',\n",
        "      extract = True,\n",
        "      cache_dir = 'C:/Users/Kristen/Desktop/DataSets/TrainingFiles/Manager1/',\n",
        ")\n",
        "\n",
        "commands = npy.array(tf.io.gfile.listdir(str(data_dir)))\n",
        "commands = commands[(commands != 'README.md') & (commands != '.DS_Store')]\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 332
        },
        "id": "M_7-_RdAyvLa",
        "outputId": "d61c5fbc-adff-4173-8e5f-b3ffe7c2b365"
      },
      "execution_count": 53,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NotFoundError",
          "evalue": "Could not find directory C:\\Users\\Kristen\\Desktop\\DataSets\\TrainingFiles\\Manager1",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNotFoundError\u001b[0m                             Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-53-bda1ec5f49c5>\u001b[0m in \u001b[0;36m<cell line: 11>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      9\u001b[0m )\n\u001b[1;32m     10\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 11\u001b[0;31m \u001b[0mcommands\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnpy\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0marray\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mio\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgfile\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlistdir\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdata_dir\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     12\u001b[0m \u001b[0mcommands\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcommands\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcommands\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0;34m'README.md'\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m&\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mcommands\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0;34m'.DS_Store'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/tensorflow/python/lib/io/file_io.py\u001b[0m in \u001b[0;36mlist_directory_v2\u001b[0;34m(path)\u001b[0m\n\u001b[1;32m    766\u001b[0m   \"\"\"\n\u001b[1;32m    767\u001b[0m   \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mis_directory\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpath\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 768\u001b[0;31m     raise errors.NotFoundError(\n\u001b[0m\u001b[1;32m    769\u001b[0m         \u001b[0mnode_def\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    770\u001b[0m         \u001b[0mop\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNotFoundError\u001b[0m: Could not find directory C:\\Users\\Kristen\\Desktop\\DataSets\\TrainingFiles\\Manager1"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "train_ds, val_ds = tf.keras.utils.audio_dataset_from_directory(\n",
        "    directory = data_dir,\n",
        "    batch_size = x,\n",
        "    validation_split = 0.1,\n",
        "    seed = 0,\n",
        "    subset = 'train'\n",
        ")"
      ],
      "metadata": {
        "id": "B2khtZ7JZlon"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train_ds.element_spec\n",
        "def squeeze(audio, labels):\n",
        "  audio = tf.squeeze(audio, axis = -1)\n",
        "  return audio, labels\n",
        "\n",
        "train_ds = train_ds.map(squeeze, tf.data.AUTOTUNE)\n",
        "val_ds = val_ds.map(squeeze, tf.data.AUTOTUNE)"
      ],
      "metadata": {
        "id": "8OaNt-olgAav"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "test_ds = val_ds.shard(num_shards = 2, index = 0)\n",
        "val_ds = val_ds.shard(num_shards = 2, index = 1)\n"
      ],
      "metadata": {
        "id": "4V4WToaRZlzr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def get_spectrogram(waveform):\n",
        "  spectrogram = tf.signal.sft(waveform, frame_length = 255, frame_step = 128)\n",
        "  spectrogram = tf.abs(spectrogram)\n",
        "  spectrogram = spectrogram[tf.newaxis]\n",
        "  return spectrogram\n",
        "\n",
        "\n",
        "plt.figure(figsize=(16, 10))\n",
        "rows = 3\n",
        "cols = 3\n",
        "n = rows * cols\n",
        "for i in range(n):\n",
        "    plt.subplot(rows, cols, i+1)\n",
        "    audio_signal = input_shape[i]\n",
        "    plt.plot(audio_signal)\n",
        "    plt.title(label_names[transcrption[i]])\n",
        "    plt.yticks(npy.arange(-1.2, 1.2, 0.2))\n",
        "    plt.ylim([-1.1, 1.1])\n",
        "\n",
        "\n",
        "for i in range(3):\n",
        "    label = label_names[prediction_label[i]]\n",
        "    waveform = input_shape[i]\n",
        "    spectrogram = get_spectrogram(waveform)\n",
        "\n",
        "def plot_spectrogram(spectrogram, ax):\n",
        "  if len(spectrogram.shape) > 2:\n",
        "    assert len(spectrogram.shape) == 3\n",
        "    spectrogram = npy.squeeze(spectrogram, axis = -1)\n",
        "    log_spec = npy.log(spectrogram.T + npyfinfo(float).eps)\n",
        "    height = log_spec.shape[0]\n",
        "    width = log_spec.shape[1]\n",
        "    X = npy.linspace(0, npy.size(spectrogram), num = width, dtype=int)\n",
        "    Y = range(height)\n",
        "    ax.pcolormesh(X, Y, log_spec)\n",
        "\n",
        "fig, axes = plt.subplots(2, figsize=(12, 8))\n",
        "timescale = npy.arange(waveform.shape[0])\n",
        "axes[0].plot(timescale, waveform.numpy())\n",
        "axes[0].set_title('Waveform')\n",
        "axes[0].set_xlim([0, 16000])\n",
        "\n",
        "plot_spectrogram(spectrogram.numpy(), axes[1])\n",
        "axes[1].set_title('Spectrogram')\n",
        "plt.suptitle(label.title())\n",
        "plt.show()\n",
        "\n",
        "\n",
        "print('Label:', label)\n",
        "print('Waveform shape:', waveform.shape)\n",
        "print('Spectrogram shape:', spectrogram.shape)\n",
        "print('Audio playback')\n",
        "display.display(display.Audio(waveform, rate=16000))\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 486
        },
        "id": "hv5qVSaWZl-U",
        "outputId": "10b2ab7f-f721-4c7d-81ac-ace718ba8b96"
      },
      "execution_count": 56,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "name 'input_shape' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-56-5bd669d6ce25>\u001b[0m in \u001b[0;36m<cell line: 12>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     12\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mn\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     13\u001b[0m     \u001b[0mplt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msubplot\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrows\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcols\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mi\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 14\u001b[0;31m     \u001b[0maudio_signal\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput_shape\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     15\u001b[0m     \u001b[0mplt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mplot\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0maudio_signal\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     16\u001b[0m     \u001b[0mplt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtitle\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlabel_names\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mtranscrption\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'input_shape' is not defined"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1600x1000 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def make_spec_ds(ds):\n",
        "  return ds.map(\n",
        "      map_func = lambda audia, label: (get_spectrogram(audio), label),\n",
        "      num_parallel_calls=tf.data.AUTOTUNE)"
      ],
      "metadata": {
        "id": "QOoN0wI2lq2I"
      },
      "execution_count": 57,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train_specrtogram_ds = train_spectrogram_ds.cache().shuffle(10000).prefetch(tf.data.AUTOTUNE)\n",
        "val_spectrogram_ds = val_spectrogram_ds.cache().prefetch(tf.data.AUTOTUNE)\n",
        "test_spectrogram_ds = test_spectrogram_ds.cache().prefetch(tf.data.AUTOTUNE)\n",
        "\n",
        "for example_spectrograms, example_spect_labels in train_specrtogram_ds.take(1):\n",
        "  break"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 228
        },
        "id": "iw3sF4Ullq7K",
        "outputId": "7bbdf729-1efb-4302-fe6b-9c3d9cdfd51a"
      },
      "execution_count": 58,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "name 'train_spectrogram_ds' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-58-3b558723a8d5>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mtrain_specrtogram_ds\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtrain_spectrogram_ds\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcache\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshuffle\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m10000\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mprefetch\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mAUTOTUNE\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mval_spectrogram_ds\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mval_spectrogram_ds\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcache\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mprefetch\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mAUTOTUNE\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mtest_spectrogram_ds\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtest_spectrogram_ds\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcache\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mprefetch\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mAUTOTUNE\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mexample_spectrograms\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexample_spect_labels\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mtrain_specrtogram_ds\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtake\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'train_spectrogram_ds' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "input_shape = example_spectrograms.shape[1:]\n",
        "print('Input shape:', input_shape)\n",
        "num_labels = len(label_names)\n",
        "\n",
        "norm_layer = tf.keras.layers.Normalization()\n",
        "norm_layer.adapt(data = train_spectrogram_ds.map(map_func = lambda spec, label: spec))\n",
        "\n",
        "model = tf.keras.models.Sequential([\n",
        "    tf.keras.layer.Input(shape = input_shape),\n",
        "    tf.keras.layer.Resizing(32, 32),\n",
        "    norm_layer,\n",
        "    tf.keras.layer.Conv2D(32, 3, activation = 'relu'),\n",
        "    tf.keras.layers.Conv2D(64, 3, activation='relu'),\n",
        "    tf.keras.layers.MaxPooling2D(),\n",
        "    tf.keras.layer.Dropout(0.25),\n",
        "    tf.keras.layer.Flatten(),\n",
        "    tf.keras.layer.Dense(128, activation='relu'),\n",
        "    tf.keras.layer.Dropout(0.5),\n",
        "    tf.keras.layer.Dense(num_labels),\n",
        "])\n",
        "\n",
        "model.summary()\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 211
        },
        "id": "o1Nfil6AuIke",
        "outputId": "e6d6ae4c-7f87-4db4-e174-8634f15e1990"
      },
      "execution_count": 59,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "name 'example_spectrograms' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-59-8cf68ba0236d>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0minput_shape\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mexample_spectrograms\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshape\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Input shape:'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0minput_shape\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mnum_labels\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlabel_names\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0mnorm_layer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mkeras\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlayers\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNormalization\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'example_spectrograms' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "model.compile(\n",
        "    optimizer=tf.keras.optimizers.Adam(),\n",
        "    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True),\n",
        "    metrics = ['accuracy']\n",
        ")\n",
        "\n",
        "EPOCHS = 10\n",
        "history = model.fit(\n",
        "    train_spectrogram_ds,\n",
        "    validation_data = val_spectrogram_ds,\n",
        "    epochs = EPOCHS,\n",
        "    callbacks=tf.keras.callbacks.EarlyStopping(verbose = 1, patience = 2),\n",
        "\n",
        ")"
      ],
      "metadata": {
        "id": "I2LdWoiehSzn"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "metrics = history.history\n",
        "plt.figure(figsize=(16,6))\n",
        "plt.subplot(1,2,1)\n",
        "plt.plot(history.epoch, metrics['loss'], metrics['val_loss'])\n",
        "plt.legend(['loss', 'val_loss'])\n",
        "plt.ylim([0, max(plt.ylim())])\n",
        "plt.xlabel('Epoch')\n",
        "plt.ylabel('Loss [CrossEntropy]')\n",
        "\n",
        "plt.subplot(1,2,2)\n",
        "plt.plot(history.epoch, 100*npy.array(metrics['accuracy']), 100*npy.array(metrics['val_accuracy']))\n",
        "plt.legend(['accuracy', 'val_accuracy'])\n",
        "plt.ylim([0, 100])\n",
        "plt.xlabel('Epoch')\n",
        "plt.ylabel('Accuracy [%]')\n",
        "\n",
        "model.evaluate(test_spectrogram_ds, return_dict = True)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 211
        },
        "id": "ApbqejYdAmMn",
        "outputId": "732c1d1d-5a07-4636-fa4e-a6946d3e4a4a"
      },
      "execution_count": 60,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "name 'history' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-60-e481b093ef00>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mmetrics\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mhistory\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhistory\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mplt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfigure\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfigsize\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m16\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m6\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mplt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msubplot\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mplt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mplot\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mhistory\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mepoch\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmetrics\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'loss'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmetrics\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'val_loss'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0mplt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlegend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'loss'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'val_loss'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'history' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred = model.predict(test_spectrogram_ds)\n",
        "y_pred= tf.argmax(y_pred, axis = 1)\n",
        "y_true = tf. concat(list(test_spectrogram_ds.map(lambda s, lab: lab)), axis = 0)\n",
        "\n",
        " confusion_mtx = tf.math.confusion_matrix(y_true, y_pred)\n",
        " plt.figure(figsize = (10, 8))\n",
        " sns.heatmap(confusion_mtx,\n",
        "             xticklabels = label_names,\n",
        "             yticklabels = label_names,\n",
        "             annot = True, fmt = 'g')\n",
        " plt.xlabel('Prediction')\n",
        " plt.ylabel('Label')\n",
        " plt.show"
      ],
      "metadata": {
        "id": "9_tND58ICC4t"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#class ExportModel(tf.Module):\n",
        "#  def __init__(self, model):\n",
        " #   self.model = model\n",
        "#\n",
        "    # Accept either a string-filename or a batch of waveforms.\n",
        "    # YOu could add additional signatures for a single wave, or a ragged-batch.\n",
        " #   self.__call__.get_concrete_function(\n",
        "  #      x=tf.TensorSpec(shape=(), dtype=tf.string))\n",
        "   # self.__call__.get_concrete_function(\n",
        "  #     x=tf.TensorSpec(shape=[None, 16000], dtype=tf.float32))\n",
        "\n",
        "\n",
        " # @tf.function\n",
        " # def __call__(self, x):\n",
        "    # If they pass a string, load the file and decode it.\n",
        " #   if x.dtype == tf.string:\n",
        "  #    x = tf.io.read_file(x)\n",
        "   #   x, _ = tf.audio.decode_wav(x, desired_channels=1, desired_samples=16000,)\n",
        "    #  x = tf.squeeze(x, axis=-1)\n",
        " #     x = x[tf.newaxis, :]\n",
        "\n",
        "  #  x = get_spectrogram(x)\n",
        "  #  result = self.model(x, training=False)\n",
        "\n",
        "   # class_ids = tf.argmax(result, axis=-1)\n",
        "   # class_names = tf.gather(label_names, class_ids)\n",
        "  #  return {'predictions':result,\n",
        "          #  'class_ids': class_ids,\n",
        "          #  'class_names': class_names}"
      ],
      "metadata": {
        "id": "pbKoLt2lCC9u"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#export = ExportModel(model)\n",
        "#export(tf.constant(str(data_dir/"
      ],
      "metadata": {
        "id": "MM97baVaCDA8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "gAbmqH77CDIN"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}