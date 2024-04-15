from SRI_IP.src.model import solve_SRI, OptimalityCriteria
from SRI_IP.src.utils import read_instance

print(solve_SRI("random_5each.txt", OptimalityCriteria.EGALITARIAN))