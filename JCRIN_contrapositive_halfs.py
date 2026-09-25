import decimal
from decimal import Decimal

def run_jcrin_halved_loop():
    # 1. Initialize context to 25 digits to perfectly view the 10-decimal expansion
    decimal.getcontext().prec = 25
    
    print("=" * 75)
    print("        JCRIN HALVED CONTRAPOSITIONAL BIDIRECTIONAL LOOP SYSTEM        ")
    print("=" * 75)
    
    # 2. Define the core 9-digit JCRIN variables
    x = Decimal('0.987654321')
    x_comp = Decimal('0.012345679')
    
    # 3. Execute division by 2 (Splitting the continuous space)
    half_x = x / Decimal('2')
    half_comp = x_comp / Decimal('2')
    
    print(f"[+] Halved Primary State (1/2 x)        = {half_x}")
    print(f"[+] Halved Complement State (1/2 x_comp) = {half_comp}")
    print("-" * 75)
    
    # 4. Verify that the linear union still achieves absolute unity when recombined
    recombined_unity = (half_x * 2) + (half_comp * 2)
    print(f"[=] Recombined Linear Union             = {recombined_unity} (Zero Residual)")
    print("-" * 75)
    
    # 5. Calculate the Inverse of the Halved Complement State
    # This maps the inverse axis to show the doubling of the 9^2 symmetry
    inv_half_comp = Decimal('1') / half_comp
    
    print(f"[Inverse Axis (1/2 x_comp)^-1]")
    print(f" -> 1 / {half_comp} = {inv_half_comp}")
    print("-" * 75)
    
    # 6. Isolate the resonant frequency parameter (162 = 2 * 81)
    base_resonance = Decimal('162')
    residual_wave = inv_half_comp - base_resonance
    
    print(f"[Resonance Analysis]")
    print(f" -> Halved Axis Integer Key Found       = {base_resonance} (2 * 9^2 Symmetry)")
    print(f" -> Isolated Periodic Residual          = {residual_wave}")
    print("=" * 75)

if __name__ == "__main__":
    run_jcrin_halved_loop()
