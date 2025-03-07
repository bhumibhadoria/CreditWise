import React from 'react';
import { useLocation } from 'react-router-dom';
import { Typography, Paper } from '@mui/material';
import { styled } from '@mui/system';

const StyledPaper = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(3),
  margin: theme.spacing(3),
}));

function ResultDisplay() {
  const location = useLocation();
  const { result } = location.state || {};

  if (!result) {
    return <Typography>No result to display</Typography>;
  }

  return (
    <StyledPaper>
      <Typography variant="h5" gutterBottom>
        Risk Assessment Result
      </Typography>
      <Typography>
        Risk Score: {result.risk_score.toFixed(2)}
      </Typography>
      <Typography>
        Recommendation: {result.recommendation}
      </Typography>
    </StyledPaper>
  );
}

export default ResultDisplay;
