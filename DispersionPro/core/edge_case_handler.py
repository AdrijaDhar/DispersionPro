# core/edge_case_handler.py

from core.briggs_plume import BriggsPlumeModel
from core.gaussian_puff import GaussianPuffModel
from core.pasquill_gifford import PasquillGiffordModel

class EdgeCaseHandler:
    def select_model(self, input_data):
        # Process input data to determine appropriate model and case
        if input_data['wind'] == 0 and input_data['continuous']:
            return BriggsPlumeModel.steady_state_no_wind(input_data['Qm'], input_data['K'], input_data['r'])
        elif input_data['wind'] == 0 and input_data['puff']:
            return GaussianPuffModel.puff_no_wind(input_data['Qm'], input_data['K'], input_data['r'], input_data['t'])
        elif input_data['wind'] != 0 and input_data['puff']:
            return GaussianPuffModel.puff_with_wind(input_data['Qm'], input_data['wind'], 
                                                    input_data['Kx'], input_data['Ky'], input_data['Kz'],
                                                    input_data['x'], input_data['y'], input_data['z'], input_data['t'])
        # Add other cases as needed
        else:
            raise ValueError("No matching model found for the given input conditions.")
