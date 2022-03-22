from typing import List, Tuple
from scipy import fftpack
import numpy as np



def fourier_transform_and_scale(signal_matrix: np.ndarray, nr_of_points: int, verbose:bool = False) -> np.ndarray:
    '''
    Fouriertransformerar en inputmatris där varje rad i matrisen är en egen elektrisk signal. 
    Ger tillbaks absolutbelopp för amplituder (styrka) hos varje frekvens. Värdet i varje index k svarar mot frekvensen
    k i den returnerade datan - det vill säga att absolute_values[2,4] motsvarar amplituden för 4 Hz i signal 2.

    Args in: signal_matrix - data för elektriska signaler
             nr_of_points - dimension för mätserie (antal mätpunkter)
             verbose - verboseflag
    Returns: scaled_ft_matrix - Fouriertransformerad matris för styrka hos olika frekvenser
    '''
    #Använder Fouriertransform för att omvandla signalerna från tidsplanet till frekvensplanet (exakta teorin är inte central just nu :))
    fourier_transformed_matrix = fftpack.fft(signal_matrix)
    if verbose:
        print(f'Shape before transform: {signal_matrix.shape}')
        print(f'Shape after transform:{fourier_transformed_matrix.shape}')

    #Har nu en matris med komplexa värden - vi är intresserade av absolutbeloppen för varje komplext värde.
    fourier_transformed_matrix = np.abs(fourier_transformed_matrix[:,:nr_of_points//2])

    #Skala alla värden för att få korrekta amplituder
    scaled_fourier_transformed_matrix = 2/nr_of_points*fourier_transformed_matrix

    return(scaled_fourier_transformed_matrix)


#Alias för type hinting
FloatVector = List[float]
TupleList = List[Tuple[int,float]]

def argmax_n(nr_of_values: int, absolute_values: FloatVector, verbose: bool = False) -> TupleList:
    '''
    Tar in en vektor utav absolutbeloppen (amplituderna), ger tillbaks lista med par av (index, value)
    index där vi stöter på högst värde. Absolutbeloppen är aldrig mindre än 0!

    Args in: nr_of_values - det antal av starkaste frekvenserna för signalen vi vill ha
             absolute_values - amplituden för varje frekvens (styrka hos signalen)
             verbose - verboseflag för output i command prompt

    Returns: maximum_frequencies - de nr_of_values starkaste signalerna med frekvens
    '''

    assert nr_of_values > 0, "Must specify a value greater than 0."
    assert len(absolute_values) >= nr_of_values, "Length of absolute_values lower than nr_of_values."
    maximum_frequencies = []
    for i in range(nr_of_values):
        #Plocka ut index för värdet med högst absolutbelopp
        current_max_index = np.argmax(absolute_values)
        value = absolute_values[current_max_index]
        maximum_frequencies.append((current_max_index, value))
        #Vi uppdaterar värdet här till 0 så att vi inte drar samma igen
        absolute_values[np.argmax(absolute_values)] = 0
    if verbose:
        print(f'Index, value pairs for frequencies and amplitudes: {maximum_frequencies}')
    return maximum_frequencies

def generate_filtered_signal(decomposed_signals: List[Tuple[float,float]], measure_range: np.array, num_columns: int) -> np.array:
    '''
    Återskapar en filtrerad, elektrisk signal av de amplituder och frekvenser som skickas in.

    Args in: decomposed_signals - Par med frekvens och amplitud för varje signal
             measure_range - tidsintervall för signalerna
             num_columns - antal punkter att skicka tillbaks
             

    Returns: filtered_signal - elektrisk signal med filtrerade värden.
    '''
    filtered_signal = np.zeros(num_columns)
    for freq_amp_tuple in decomposed_signals:
        freq, amplitude = freq_amp_tuple
        freq*= 2*np.pi
        filtered_signal += amplitude*np.sin(freq*measure_range)
    return filtered_signal
