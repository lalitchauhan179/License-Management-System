const axios = require('axios');

const validateLicense = async (req, res, next) => {
  const licenseKey = req.headers['x-license-key'];
  
  if (!licenseKey) {
    return res.status(401).json({ message: "License key missing" });
  }

  try {
    const response = await axios.post('http://yourserver.com/license/validate', {
      license_key: licenseKey,
    });

    if (response.status === 200) {
      next(); // License valid, proceed to next middleware
    } else {
      return res.status(401).json({ message: "Invalid license" });
    }
  } catch (error) {
    return res.status(500).json({ message: "Error validating license" });
  }
};

module.exports = validateLicense;
