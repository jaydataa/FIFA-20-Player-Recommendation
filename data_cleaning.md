## Data Cleaning Process  

The dataset had missing values, unnecessary columns, and inconsistent formats.  

### Key Fixes:
1. **Dropped irrelevant columns** (e.g., `body_type`, `loaned_from`).
2. **Filled missing values** in `club` with "Free Agent".
3. **Converted height & weight to integers** for consistency.
4. **Renamed columns** to lowercase for easier access.

### Data Before Cleaning:
| Column     | Missing Values | Example Value |
|------------|---------------|---------------|
| club       | 400           | Manchester City |
| weak_foot  | 200           | 4             |

### Data After Cleaning:
| Column     | Missing Values | Example Value |
|------------|---------------|---------------|
| club       | 0             | Manchester City |
| weak_foot  | 0             | 4             |

