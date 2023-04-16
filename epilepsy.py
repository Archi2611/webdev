import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:/Users/Aman Sinha/Downloads/epilepsy_model.sav', 'rb'))


# creating a function for Prediction

def epilepsy_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'You do not have Epilepsy'
    else:
      return 'You have Epilepsy'
  
    
  
def main():
    
    
    # giving a title
    st.title('Epilepsy Prediction Web App')
    
    
    # getting the input data from the user
    
    
    EEG_after_1_second = st.text_input('X1')
    EEG_after_2_second = st.text_input('X2')
    EEG_after_3_second = st.text_input('X3')
    EEG_after_4_second = st.text_input('X4')
    EEG_after_5_second = st.text_input('X5')
    EEG_after_6_second = st.text_input('X6')
    EEG_after_7_second = st.text_input('X7')
    EEG_after_8_second = st.text_input('X8')
    EEG_after_9_second = st.text_input('X9')
    EEG_after_10_second = st.text_input('X10')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    
    if st.button('Epilepsy Test Result'):
        diagnosis = epilepsy_prediction([Average_vocal_fundamental_frequency, Maximum_vocal_fundamental_frequency, Minimum_vocal_fundamental_frequency, variation_in_fundamental_frequency1, variation_in_fundamental_frequency2, variation_in_fundamental_frequency3, variation_in_fundamental_frequency4, variation_in_fundamental_frequency5, measures_of_variation_in_amplitude1, measures_of_variation_in_amplitude2, measures_of_variation_in_amplitude3, measures_of_variation_in_amplitude4, measures_of_variation_in_amplitude5, measures_of_variation_in_amplitude6, measures_of_the_ratio_of_noise_to_tonal_components_in_the_voice1, measures_of_the_ratio_of_noise_to_tonal_components_in_the_voice2, nonlinear_dynamical_complexity_measures1, nonlinear_dynamical_complexity_measures2, Signal_fractal_scaling_exponent, nonlinear_measures_of_fundamental_frequency_variation1, nonlinear_measures_of_fundamental_frequency_variation2, nonlinear_measures_of_fundamental_frequency_variation3])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
