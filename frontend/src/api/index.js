import axios from 'axios';

const API_URL = 'http://localhost:8000'; // Adjust this to your backend URL

export const assessRisk = async (data) => {
  try {
    const response = await axios.post(`${API_URL}/predict`, data);
    return response.data;
  } catch (error) {
    console.error('Error assessing risk:', error);
    throw error;
  }
};
