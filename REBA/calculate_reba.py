import numpy as np
import neck_reba_score as RebaNeck
import trunk_reba_score as RebaTrunk
import leg_reba_score as RebaLeg
import upper_arm_score as UpperArm
import lower_arm_score as LowerArm
import wrist_score as Wrist

#from scripts.calculate_angles import CalculateAngles

class DegreetoREBA:
    def __init__(self, joints_degree):
        self.joints_degree = joints_degree

    def reba_table_a(self):
        return np.array([
            [[1, 2, 3, 4], [2, 3, 4, 5], [2, 4, 5, 6], [3, 5, 6, 7], [4, 6, 7, 8]],
            [[1, 2, 3, 4], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9]],
            [[3, 3, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9, 9]]
        ])
    
    def reba_table_b(self):
        return np.array([
            [[1, 2, 2], [1, 2, 3]],
            [[1, 2, 3], [2, 3, 4]],
            [[3, 4, 5], [4, 5, 5]],
            [[4, 5, 5], [5, 6, 7]],
            [[6, 7, 8], [7, 8, 8]],
            [[7, 8, 8], [8, 9, 9]],
        ])

    def reba_table_c(self):
        return np.array([
            [1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 7, 7],
            [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8],
            [2, 3, 3, 3, 4, 5, 6, 7, 7, 8, 8, 8],
            [3, 4, 4, 4, 5, 6, 7, 8, 8, 9, 9, 9],
            [4, 4, 4, 5, 6, 7, 8, 8, 9, 9, 9, 9],
            [6, 6, 6, 7, 8, 8, 9, 9, 10, 10, 10, 10],
            [7, 7, 7, 8, 9, 9, 9, 10, 10, 11, 11, 11],
            [8, 8, 8, 9, 10, 10, 10, 10, 10, 11, 11, 11],
            [9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12],
            [10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 12],
            [11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12],
            [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
        ])
    def reba_computation(self):
        # Table A ( Neck X Trunk X Legs)
        table_a = self.reba_table_a()
        # Table B ( UpperArm X LowerArm X Wrist)
        table_b = self.reba_table_b()
        # Table C ( ScoreA X ScoreB)
        table_c = self.reba_table_c()

        # step1: locate neck position
        neck_degrees = self.joints_degree[0]
        m_neck_REBA = RebaNeck.NeckREBA(neck_degrees)
        neck_scores = m_neck_REBA.neck_reba_score()

        # step2: locate trunck posture
        # trunk_degrees = self.joints_degree[1]
        # m_trunk_REBA = RebaTrunk.TrunkREBA(trunk_degrees)
        # trunk_scores = m_trunk_REBA.trunk_reba_score()

        # # step3: locate legs
        # leg_degrees = [self.joints_degree[2], self.joints_degree[3]]
        # m_leg_REBA = RebaLeg.LegREBA(leg_degrees)
        # leg_scores = m_leg_REBA.leg_reba_score()
        # # leg_scores =[1]

        # # step 4: Look up score in table _A
        # if neck_scores[0] - 1>2:
        #     neck_scores[0] = 3
        # if trunk_scores[0] - 1>4:
        #     trunk_scores[0]  = 5
        # if leg_scores[0] - 1>3:
        #     leg_scores[0] = 4
        
        # posture_score_a = table_a[neck_scores[0] - 1][trunk_scores[0] - 1][leg_scores[0] - 1]

        # # step 5: load score in kg
        # # load = input("what is the load(in kg) ")
        # load = 5
        # if 5 <= int(load) < 10:
        #     posture_score_a = posture_score_a + 1
        # if 10 <= int(load):
        #     posture_score_a = posture_score_a + 2
        
        # # step 7: upper arm score
        # UA_degrees = self.joints_degree[3]
        # m_upper_arm_REBA = UpperArm.UAREBA(UA_degrees)
        # UA_scores = m_upper_arm_REBA.upper_arm_reba_score()

        # # step 8: lower arm score
        # LA_degrees = self.joints_degree[4]
        # m_lower_arm_REBA = LowerArm.LAREBA(LA_degrees)
        # LA_scores = m_lower_arm_REBA.lower_arm_score()

        # # step 9: wrist score
        # wrist_degrees = self.joints_degree[5]
        # m_wrist_REBA = Wrist.WristREBA(wrist_degrees)
        # wrist_scores = m_wrist_REBA.wrist_reba_score()

        # # step 10: Look up score in table _B
        # posture_score_b = table_b[UA_scores[0] - 1][LA_scores - 1][wrist_scores[0] - 1]

        # # step 11: coupling score
        # #  assume coupling is 2
        # coupling = 2
        # # coupling = input("what is the coupling condition?(good(0) or fair(1) or poor(2) or unacceptable(3)? ")

        # posture_score_b = posture_score_b + int(coupling)

        # # step 12: look up score in table C
        # posture_score_c = table_c[posture_score_a - 1][posture_score_b - 1]

        #return(f"Score for table A is: {posture_score_a}")
        return(f"Neck score is: {neck_scores}")
    
#joints_degree = [30, 80, 20, 15]
# joints_degree = []
# classA_obj = DegreetoREBA(joints_degree)
# A_reba_score = classA_obj.reba_computation()
# print(A_reba_score)