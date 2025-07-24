# wearipedia-data

## Introduction

This repo makes all [Wearipedia](https://www.wearipedia.com) device data downloadable as .json files. Specifically, `devices.json` contains the full list of devices and corresponding data that is used in the website.

To add or edit existing data for a new device, submit a pull request to this repo with specifications for the new device under `/devices`. To understand the schema, refer to the [Devices](#Devicesjson) section below.

## Devices

Each wearable available on the website is listed under `devices.json` with the schema below.

<details><summary>devices schema</summary>

```
const mongoose = require('mongoose');

const wearablesSchema = new mongoose.Schema({
  name: {
    type: String,
    // required: true
  },
  id: {
    type: String,
    // required: true,
    unique: true,
    dropDups: true
  },
  ordering_priority: {
    type: Number
    // required: true
  },
  picture: {
    type: String,
    // required: true
  },
  description: {
    type: String,
    // required: true
  },
  next: {
    name: String,
    id: String
  },
  tags: [mongoose.Schema.Types.ObjectId],
  notebooks: [{
    name: {
      type: String,
      // required: true
    },
    link: {
      type: String,
      // required: true
    }
  }],
  link: {
    type: String,
    // required: true
  },
  specs: {
    product_details: {
      Location: {
        type: String,
        // required: true
        ordering_priority: { type: Number, default: 0 }
      },
      Price: {
        type: String,
        // required: true
        ordering_priority: { type: Number, default: 1 }
      },
      Sensors: [String],
      Battery: {
        type: String,
        // required: true
        ordering_priority: { type: Number, default: 2 }
      }
    },
    security: {
      'Wearable Connectivity': {
        short: {
          type: String,
          // required: true
        },
        long: {
          type: String,
          // required: true
        },
        ordering_priority: { type: Number, default: 3 }
      },
      'API Access Security': {
        short: {
          type: String,
          // required: true
        },
        long: {
          type: String,
          // required: true
        },
        ordering_priority: { type: Number, default: 4 }
      }
    },
    privacy: {
      'Data Risk': {
        short: {
          type: String,
          // required: true
        },
        long: {
          type: String,
          // required: true
        },
        ordering_priority: { type: Number, default: 5 }
      },
      'HIPAA Compliance': {
        short: {
          type: String,
          // required: true
        },
        long: {
          type: String,
          // required: true
        },
        ordering_priority: { type: Number, default: 6 }
      },
      'De-identification (When Sharing)': {
        short: {
          type: String,
          // required: true
        },
        long: {
          type: String,
          // required: true
        },
        ordering_priority: { type: Number, default: 7 }
      },
      'Shares With Third Parties': {
        short: {
          type: String,
          // required: true
        },
        long: {
          type: String,
          // required: true
        },
        ordering_priority: { type: Number, default: 8 }
      },
      'Transparency in Third Party Sharing': {
        short: {
          type: String,
          // required: true
        },
        long: {
          type: String,
          // required: true
        },
        ordering_priority: { type: Number, default: 9 }
      }
    }
  },
  api: {
    daytime: {
      type: [Array],
      // required: true
    },
    nighttime: {
      type: [Array],
      // required: true
    },
    sensor_performance: {
      type: [Array],
      // required: true
    }
  },
  summaries: [String]
});

const Wearables = mongoose.model('Wearables', wearablesSchema);

module.exports = Wearables;
```
</details>
<br />

An instance of the above schema can be found under `/devices/abbott-freestyle-libre.json` (also provided below).

<br />
<details><summary>abbott-freestyle-libre.json</summary>

```
{
    "name": "Abbott Freestyle Libre",
    "id": "abbott-freestyle-libre",
    "ordering_priority": 6,
    "picture": "/assets/abbott-freestyle-libre.png",
    "description": "The Abbott FreeStyle Libre is an advanced continuous glucose monitoring (CGM) system, essential for diabetes management. It features a discreet sensor attached to the upper arm, providing real-time glucose readings for up to 14 days. The sensor measures glucose levels in interstitial fluid, offering a less invasive alternative to traditional fingerstick tests. Users can scan the sensor with a dedicated reader or a smartphone app, which also provides optional alarms for hypo- and hyperglycemia. This CGM system is crucial for individuals with diabetes, enabling them to monitor glucose trends and patterns effectively. The FreeStyle Libre 2 aids in better diabetes management by allowing patients and healthcare providers to adjust treatments based on comprehensive glucose data. Its impact on diabetes care is significant, making it a valuable tool in both personal health management and medical research in endocrinology.",
    "tags": ["CGM"],
    "notebooks": [],
    "link": "https://www.freestyle.abbott/us-en/products/freestyle-libre-2.html",
    "specs": {
      "product_details": {
        "Location": "Back of upper arm",
        "Price": "$0.00 - $75.00 / month",
        "Sensors": [],
        "Battery": ""
      },
      "security": {
        "Wearable Connectivity": {
          "short": "Yes",
          "long": "Near-field communication."
        },
        "API Access Security": {
          "short": "N/A",
          "long": "No public API is available."
        }
      },
      "privacy": {
        "Data Risk": {
          "short": "No",
          "long": "Data from the Abbott Freestyle Libre includes continuous glucose readings. The sensor captures glucose data every minute, storing 8 hours of data at a time. When the sensor is scanned by the reader or compatible smartphone, the stored data is transferred, allowing users to view their glucose trends, peaks, and lows. The system also has optional real-time glucose alarms to notify users if glucose levels are too high or too low. <br />These data constitute a health data risk in the following categories: <br />- Physiological data: The system captures data related to hyperglycemic (high) and hypoglycemic (low) events, which can indicate potential health concerns or the need for treatment adjustments. <br />- Health status data: Continuous glucose readings, reflecting the individual's real-time and historical blood sugar levels, patterns of glucose fluctuations, allowing users to understand how different factors, such as meals, stress, or physical activity, impact their glucose levels. <br />- Predictive health insights: Based on glucose trends and patterns, users can adjust their dietary, medication, or lifestyle choices to optimize their glucose management and overall health."
        },
        "HIPAA Compliance": {
          "short": "No",
          "long": "Abbott Freestyle Libre collects glucose levels at frequent intervals, and this data is transmitted to its designated reader or compatible smart device. <br />Glucose data, due to its direct relevance to an individual's health status, could be considered protected health information under HIPAA. <br />Abbott Freestyle Libre is not HIPAA compliant."
        },
        "De-identification (When Sharing)": {
          "short": "Yes",
          "long": "Abbott may share your personal information with third parties with whom Abbott is jointly marketing a product or service or jointly conducting a program or activity."
        },
        "Shares With Third Parties": {
          "short": "No",
          "long": "Abbott Freestyle Libre mentions that they 'will not sell or license personal data to third parties except in connection with the sale or transfer of a product line or division, or in connection with a joint marketing program'. <br />This raises concerns about the specific conditions under which user data might be shared or transferred, especially since such broad provisions might encompass a variety of scenarios where data can be shared without explicit user consent."
        },
        "Transparency in Third Party Sharing": {
          "short": "No",
          "long": "Categories of third parties are vaguely referenced in connection with 'the sale or transfer of a product line or division' or in connection with 'a joint marketing program'. <br />No mentions of specific companies, organizations, or individuals are provided."
        }
      }
    },
    "api": {},
    "summaries": [
      "Abbott_Freestyle_Libre_2_Bariatrics.txt",
      "Abbott_Freestyle_Libre_2_Cardiology.txt",
      "Abbott_Freestyle_Libre_2_ChronicPainOrDiseases.txt",
      "Abbott_Freestyle_Libre_2_Endocrinology.txt",
      "Abbott_Freestyle_Libre_2_Gastroenterology.txt",
      "Abbott_Freestyle_Libre_2_GeneralPhysiology.txt",
      "Abbott_Freestyle_Libre_2_Nephrology.txt",
      "Abbott_Freestyle_Libre_2_Obstetrics.txt",
      "Abbott_Freestyle_Libre_2_Oncology.txt",
      "Abbott_Freestyle_Libre_2_Other.txt",
      "Abbott_Freestyle_Libre_2_Psychiatry.txt",
      "Abbott_Freestyle_Libre_2_Pulmonology.txt",
      "Abbott_Freestyle_Libre_2_Somnology.txt"
    ]
}
```
</details>
<br />

Afterwards, the `devices.json` is generated during a pre-commit check (or can be executed manually by running the `generate-device-jsons.py` script).
