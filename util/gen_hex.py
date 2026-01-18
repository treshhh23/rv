import os

# --- Configuration ---
FILENAME = "memory_init.hex"
DEPTH = 64        # Match your Verilog MEM_WORDS
WIDTH_BITS = 32

# --- Logic ---

# 1. Remove the old file if it exists (Clean slate)
if os.path.exists(FILENAME):
    os.remove(FILENAME)
    print(f"Removed old {FILENAME}")

# 2. Generate the new file
try:
    with open(FILENAME, "w") as f:
        for i in range(DEPTH):
            # Writes 00000000 followed by a new line
            f.write(f"{0:08x}\n")
            
    print(f"SUCCESS: Generated {FILENAME} in the current folder.")

except IOError as e:
    print(f"ERROR: {e}")