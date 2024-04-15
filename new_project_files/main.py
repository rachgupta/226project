from SRI_IP.src.model import solve_SRI, OptimalityCriteria
from SRI_IP.src.utils import read_instance
from SRI_IP.src.feasibility_checker import check_feasibility

print(solve_SRI("random_5each.txt", OptimalityCriteria.EGALITARIAN))