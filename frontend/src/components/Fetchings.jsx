import axios from 'axios';
import React from 'react';
import API from '../api/api';

const Fetching = async () => {
  try{
  const acssesToken = localStorage.getItem('accessToken');
  const {data} = await axios.get(`${API}/`,{
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${acssesToken}`,
    },
  })
  
    console.log("Fetched Message:", data.message);
    return data.message;
  }catch(error){
    console.error("HomeFetch failed:", error.response?.data || error.message);
    return null;
  }
}

export default Fetching;
