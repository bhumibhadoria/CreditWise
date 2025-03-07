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
    income: '',         // newly added
    debt: ''            // newly added
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const payload = {
      annual_revenue: parseFloat(formData.annual_revenue) || 0,
      loan_amount: parseFloat(formData.loan_amount) || 0,
      gst_compliance: formData.gst_compliance,
      market_trend: formData.market_trend,
      credit_score: parseFloat(formData.credit_score) || 0,
      business_age: parseFloat(formData.business_age) || 0,
      industry_sector: formData.industry_sector,
      num_employees: parseFloat(formData.num_employees) || 0,
      monthly_burn_rate: parseFloat(formData.monthly_burn_rate) || 0,
      current_ratio: parseFloat(formData.current_ratio) || 0,
      income: parseFloat(formData.income) || 0,  // newly added
      debt: parseFloat(formData.debt) || 0       // newly added
    };
    try {
      const result = await assessRisk(payload);
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
        {/* New Fields */}
        <Grid item xs={12} sm={6}>
          <TextField
            name="gst_compliance"
            label="GST Compliance (High/Medium/Low)"
            fullWidth
            value={formData.gst_compliance}
            onChange={handleChange}
            required
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            name="market_trend"
            label="Market Trend (Growth/Stable/Declining)"
            fullWidth
            value={formData.market_trend}
            onChange={handleChange}
            required
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            name="credit_score"
            label="Credit Score"
            type="number"
            fullWidth
            value={formData.credit_score}
            onChange={handleChange}
            required
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            name="business_age"
            label="Business Age"
            type="number"
            fullWidth
            value={formData.business_age}
            onChange={handleChange}
            required
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            name="industry_sector"
            label="Industry Sector"
            fullWidth
            value={formData.industry_sector}
            onChange={handleChange}
            required
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            name="num_employees"
            label="Number of Employees"
            type="number"
            fullWidth
            value={formData.num_employees}
            onChange={handleChange}
            required
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            name="monthly_burn_rate"
            label="Monthly Burn Rate"
            type="number"
            fullWidth
            value={formData.monthly_burn_rate}
            onChange={handleChange}
            required
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            name="current_ratio"
            label="Current Ratio"
            type="number"
            fullWidth
            value={formData.current_ratio}
            onChange={handleChange}
            required
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            name="income"
            label="Income"
            type="number"
            fullWidth
            value={formData.income}
            onChange={handleChange}
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            name="debt"
            label="Debt"
            type="number"
            fullWidth
            value={formData.debt}
            onChange={handleChange}
          />
        </Grid>
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
