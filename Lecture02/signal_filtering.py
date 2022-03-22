import matplotlib.pyplot as plt
import pandas as pd
from signal_utils import *



def main():
    '''
    Reads data from noisy, electric signals and filters out the strongest frequencies and their
    amplitudes (signal strength). Plots the original signal, the amplitudes of filtered frequencies and
    the original signals together with filtered signals produced from the filtered data.
    '''
    verbose = True
    #Läs in signaldata från csv-filen
    data = pd.read_csv("Lecture01/data/electric_signals.csv")
    #Gör om till np.array
    data = np.array(data)

    num_rows,num_columns = data.shape
    fig, ax = plt.subplots(num_rows)
    fig.suptitle("Original electric signals")
    for i, row in enumerate(data):
        ax[i].plot(np.arange(num_columns),row)
        ax[i].set(xlabel = "Time [t]", ylabel = "Amplitude")
    plt.show()





    #Vi vill utreda vilka frekvenser som är starkast i signalerna. Kallar på fourier_transform_and_scale
    transforms = fourier_transform_and_scale(signal_matrix = data, nr_of_points = num_columns,
                                                                             verbose = verbose)

    #linspacevector att plotta amplituder i transforms mot
    xf = np.linspace(0.0, int(num_columns/2), int(num_columns/2))

    #Bestäm antal frekvenser för varje signal vi vill utreda
    nr_of_frequencies = 2
    #Stoppa resultat i en dictionary för index och amplituder
    indices_and_amplitudes = {}
    fig, ax = plt.subplots(num_rows)
    fig.suptitle("Frequency decomposition of electric signals")
    for i, row in enumerate(transforms):
        ax[i].plot(xf,row)
        ax[i].set(xlabel = "Frequency [Hz]", ylabel = "Amplitude")
        indices_and_amplitudes["Signal source " + str(i)] = argmax_n(nr_of_frequencies, transforms[i,:], verbose = verbose)
    if verbose:
        print(f'Shape of signal data: [Signals, Time point]: {data.shape}')
        for key,value in indices_and_amplitudes.items():
            print(f'Frequency/Amplitude pairs for {key}: {value}')
    plt.show()


    measure_range = np.linspace(0.0, num_columns, num_columns)


    fig, ax = plt.subplots(num_rows)
    fig.suptitle("Comparison of filtered/unfiltered signals")
    for i, row in enumerate(zip(data,indices_and_amplitudes.values())):
        original_data_row, decomposed_frequencies = row
        filtered_signal = generate_filtered_signal(decomposed_signals=decomposed_frequencies, measure_range = measure_range, num_columns = num_columns)
        ax[i].plot(np.arange(num_columns), original_data_row, label = 'Original Data')
        ax[i].plot(np.arange(num_columns), filtered_signal, label = 'Filtered Data')
        ax[i].set(xlabel = "Frequency [Hz]", ylabel = "Amplitude")
    plt.legend()
    plt.show()
    



if __name__ == "__main__":
    main()
