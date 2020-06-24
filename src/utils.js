const formatDate = (date) => {
  const dateOptions = {
    year: 'numeric',
    month: 'short',
    day: 'numeric'
  };
  return new Date(date).toLocaleDateString('en-US', dateOptions)
};

export { formatDate };