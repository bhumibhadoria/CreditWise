import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { TextField, Button, Grid } from '@mui/material';
import { styled } from '@mui/system';
import { assessRisk } from '../api';

const StyledForm = styled('form')(({ theme }) => ({
  width: '100%',
  marginTop: theme.spacing(3),
}));

const SubmitButton = styled(Button)(({ theme }) => ({
  margin: theme.spacing(3, 0, 2),
}));

function InputForm() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    annual_revenue: '',
    loan_amount: '',
    gst_compliance: '',
    market_trend: '',
    credit_score: '',
    business_age: '',
    industry_sector: '',
    num_employees: '',
    monthly_burn_rate: '',
    current_ratio: '',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const result = await assessRisk(formData);
      navigate('/result', { state: { result } });
    } catch (error) {
      console.error('Error assessing risk:', error);
    }
  };

  return (
    <StyledForm onSubmit={handleSubmit}>
      <Grid container spacing={2}>
        <Grid item xs={12} sm={6}>
          <TextField
            name="annual_revenue"
            label="Annual Revenue"
            type="number"
            fullWidth
            value={formData.annual_revenue}
            onChange={handleChange}
            required
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            name="loan_amount"
            label="Loan Amount"
            type="number"
            fullWidth
            value={formData.loan_amount}
            onChange={handleChange}
            required
          />
        </Grid>
        {/* Add more fields here */}
      </Grid>
      <SubmitButton
        type="submit"
        fullWidth
        variant="contained"
        color="primary"
      >
        Assess Risk
      </SubmitButton>
    </StyledForm>
  );
}

export default InputForm;
