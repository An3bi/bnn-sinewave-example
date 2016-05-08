# Global
import shutil
import csv

# NUPIC
from nupic.swarming import permutations_runner
from nupic.frameworks.opf.modelfactory import ModelFactory
from nupic_output import NuPICFileOutput, NuPICPlotOutput

# Local
import generate_data

swarm_config = {
  "includedFields": [
    {
      "fieldName": "sine",
      "fieldType": "float",
      "maxValue": 1.0,
      "minValue": -1.0
    }
  ],
  "streamDef": {
    "info": "sine",
    "version": 1,
    "streams": [
      {
        "info": "sine.csv",
        "source": "file://sine.csv",
        "columns": [
          "*"
        ]
      }
    ]
  },
  "inferenceType": "TemporalAnomaly",
  "inferenceArgs": {
    "predictionSteps": [
      1
    ],
    "predictedField": "sine"
  },
  "swarmSize": "medium"
}

def swarm_over_data():
    model_params = permutations_runner.runWithConfig(swarm_config,
     {'maxWorkers': 2, 'overwrite': True})
    shutil.copyfile("model_0/model_params.py", "model_params.py")

def run_experiment():
    generate_data.run()
    swarm_over_data()
    import model_params
    model = ModelFactory.create(model_params.MODEL_PARAMS)
    model.enableInference({"predictedField": "sine"})
    output = NuPICPlotOutput("sine_out", show_anomaly_score=True)

    with open("sine.csv", "rb") as sine_input:
        csv_reader = csv.reader(sine_input)

        # Skip headers
        csv_reader.next()
        csv_reader.next()
        csv_reader.next()

        # Real Data
        for row in csv_reader:
            angle = float(row[0])
            sine_value = float(row[1])

            result = model.run({"sine": sine_value})
            output.write(angle, sine_value, result)

    output.close()

if __name__ == "__main__":
    run_experiment()
