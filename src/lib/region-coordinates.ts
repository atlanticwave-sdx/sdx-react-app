/**
 * Static lookup table for ISO 3166-2 region center coordinates.
 * Used for displaying clustered markers at official region centers
 * when the map is zoomed out.
 */

export interface RegionCoordinates {
  latitude: number;
  longitude: number;
  name: string;
}

export const ISO_3166_2_COORDINATES: Record<string, RegionCoordinates> = {
  // United States
  "US-FL": { latitude: 27.6648, longitude: -81.5158, name: "Florida" },
  "US-CA": { latitude: 36.7783, longitude: -119.4179, name: "California" },
  "US-TX": { latitude: 31.9686, longitude: -99.9018, name: "Texas" },
  "US-GA": { latitude: 32.1656, longitude: -82.9001, name: "Georgia" },
  "US-NY": { latitude: 40.7128, longitude: -74.006, name: "New York" },
  "US-IL": { latitude: 40.6331, longitude: -89.3985, name: "Illinois" },
  "US-WA": { latitude: 47.7511, longitude: -120.7401, name: "Washington" },
  "US-OR": { latitude: 43.8041, longitude: -120.5542, name: "Oregon" },
  "US-AZ": { latitude: 34.0489, longitude: -111.0937, name: "Arizona" },
  "US-NV": { latitude: 38.8026, longitude: -116.4194, name: "Nevada" },
  "US-CO": { latitude: 39.5501, longitude: -105.7821, name: "Colorado" },
  "US-NC": { latitude: 35.7596, longitude: -79.0193, name: "North Carolina" },
  "US-VA": { latitude: 37.4316, longitude: -78.6569, name: "Virginia" },
  "US-MD": { latitude: 39.0458, longitude: -76.6413, name: "Maryland" },
  "US-DC": { latitude: 38.9072, longitude: -77.0369, name: "District of Columbia" },
  "US-NJ": { latitude: 40.0583, longitude: -74.4057, name: "New Jersey" },
  "US-PA": { latitude: 41.2033, longitude: -77.1945, name: "Pennsylvania" },
  "US-MA": { latitude: 42.4072, longitude: -71.3824, name: "Massachusetts" },
  "US-OH": { latitude: 40.4173, longitude: -82.9071, name: "Ohio" },
  "US-MI": { latitude: 44.3148, longitude: -85.6024, name: "Michigan" },
  "US-TN": { latitude: 35.5175, longitude: -86.5804, name: "Tennessee" },
  "US-LA": { latitude: 30.9843, longitude: -91.9623, name: "Louisiana" },
  "US-AL": { latitude: 32.3182, longitude: -86.9023, name: "Alabama" },
  "US-SC": { latitude: 33.8361, longitude: -81.1637, name: "South Carolina" },

  // Brazil
  "BR-RJ": { latitude: -22.9068, longitude: -43.1729, name: "Rio de Janeiro" },
  "BR-SP": { latitude: -23.5505, longitude: -46.6333, name: "São Paulo" },
  "BR-RS": { latitude: -30.0346, longitude: -51.2177, name: "Rio Grande do Sul" },
  "BR-PR": { latitude: -25.4284, longitude: -49.2733, name: "Paraná" },
  "BR-SC": { latitude: -27.5954, longitude: -48.548, name: "Santa Catarina" },
  "BR-MG": { latitude: -19.9167, longitude: -43.9345, name: "Minas Gerais" },
  "BR-BA": { latitude: -12.9714, longitude: -38.5014, name: "Bahia" },
  "BR-CE": { latitude: -3.7172, longitude: -38.5433, name: "Ceará" },
  "BR-PE": { latitude: -8.0476, longitude: -34.877, name: "Pernambuco" },
  "BR-DF": { latitude: -15.7975, longitude: -47.8919, name: "Distrito Federal" },
  "BR-GO": { latitude: -16.6869, longitude: -49.2648, name: "Goiás" },
  "BR-PA": { latitude: -1.4558, longitude: -48.4902, name: "Pará" },
  "BR-AM": { latitude: -3.119, longitude: -60.0217, name: "Amazonas" },

  // South Africa
  "ZA-GT": { latitude: -26.2041, longitude: 28.0473, name: "Gauteng" },
  "ZA-WC": { latitude: -33.9249, longitude: 18.4241, name: "Western Cape" },
  "ZA-KZN": { latitude: -29.8587, longitude: 31.0218, name: "KwaZulu-Natal" },
  "ZA-EC": { latitude: -33.9608, longitude: 25.6022, name: "Eastern Cape" },
  "ZA-LP": { latitude: -23.8962, longitude: 29.4486, name: "Limpopo" },
  "ZA-MP": { latitude: -25.4653, longitude: 30.9853, name: "Mpumalanga" },
  "ZA-NW": { latitude: -25.8523, longitude: 25.6445, name: "North West" },
  "ZA-FS": { latitude: -29.0852, longitude: 26.1596, name: "Free State" },
  "ZA-NC": { latitude: -29.0467, longitude: 21.8569, name: "Northern Cape" },

  // Chile
  "CL-RM": { latitude: -33.4489, longitude: -70.6693, name: "Santiago Metropolitan" },
  "CL-VS": { latitude: -33.0472, longitude: -71.6127, name: "Valparaíso" },
  "CL-BI": { latitude: -36.8261, longitude: -73.05, name: "Biobío" },

  // Argentina
  "AR-C": { latitude: -34.6037, longitude: -58.3816, name: "Buenos Aires City" },
  "AR-B": { latitude: -34.9215, longitude: -57.9545, name: "Buenos Aires Province" },
  "AR-X": { latitude: -31.4201, longitude: -64.1888, name: "Córdoba" },
  "AR-S": { latitude: -32.9468, longitude: -60.6393, name: "Santa Fe" },

  // Colombia
  "CO-DC": { latitude: 4.711, longitude: -74.0721, name: "Bogotá" },
  "CO-ANT": { latitude: 6.2476, longitude: -75.5658, name: "Antioquia" },
  "CO-VAC": { latitude: 3.4516, longitude: -76.532, name: "Valle del Cauca" },

  // Mexico
  "MX-CMX": { latitude: 19.4326, longitude: -99.1332, name: "Mexico City" },
  "MX-JAL": { latitude: 20.6597, longitude: -103.3496, name: "Jalisco" },
  "MX-NLE": { latitude: 25.6866, longitude: -100.3161, name: "Nuevo León" },

  // Panama
  "PA-8": { latitude: 9.0402, longitude: -79.4986, name: "Panamá" },

  // Ecuador
  "EC-P": { latitude: -0.1807, longitude: -78.4678, name: "Pichincha" },
  "EC-G": { latitude: -2.1894, longitude: -79.8891, name: "Guayas" },

  // Peru
  "PE-LIM": { latitude: -12.0464, longitude: -77.0428, name: "Lima" },

  // Venezuela
  "VE-A": { latitude: 10.4806, longitude: -66.9036, name: "Capital District" },

  // Portugal
  "PT-11": { latitude: 38.7223, longitude: -9.1393, name: "Lisbon" },
  "PT-13": { latitude: 41.1579, longitude: -8.6291, name: "Porto" },

  // Spain
  "ES-MD": { latitude: 40.4168, longitude: -3.7038, name: "Madrid" },
  "ES-CT": { latitude: 41.3851, longitude: 2.1734, name: "Catalonia" },

  // Netherlands
  "NL-NH": { latitude: 52.3676, longitude: 4.9041, name: "North Holland" },

  // United Kingdom
  "GB-ENG": { latitude: 51.5074, longitude: -0.1278, name: "England" },
  "GB-LND": { latitude: 51.5074, longitude: -0.1278, name: "London" },
};

/**
 * Get coordinates for a region, with fallback to provided coordinates
 * if the region is not in the lookup table.
 */
export function getRegionCoordinates(
  regionCode: string,
  fallbackLat?: number,
  fallbackLng?: number
): { latitude: number; longitude: number } {
  const region = ISO_3166_2_COORDINATES[regionCode];
  if (region) {
    return { latitude: region.latitude, longitude: region.longitude };
  }
  return {
    latitude: fallbackLat ?? 0,
    longitude: fallbackLng ?? 0,
  };
}

/**
 * Get the human-readable name for a region code.
 */
export function getRegionName(regionCode: string): string {
  const region = ISO_3166_2_COORDINATES[regionCode];
  return region?.name ?? regionCode;
}
