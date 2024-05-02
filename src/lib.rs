use pyo3::prelude::*;
use pyo3::exceptions::PyValueError;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn find_primes_fast(up_to: i32) -> PyResult<Vec<i32>> {
    let mut primes = Vec::new();
    if up_to < 0 {
        return Err(PyValueError::new_err("'up_to' must be greater than 0"));
    }
    if up_to == 0 || up_to == 1 {
        return Ok(primes);
    }
    else if up_to == 2 {
        primes.push(2);
        return Ok(primes);
    }
    else {
        for value in 2..up_to {
            if value == 2 {
                primes.push(value)
            }
            else {
                let mut add_value = false;
                for prev in primes.iter() {
                    add_value = false;
                    if value % prev == 0 {
                        break;
                    }
                    add_value = true;
                }
                if add_value {
                    primes.push(value)
                }
            }
        }
    }

    Ok(primes)
}

/// A Python module implemented in Rust.
#[pymodule]
fn prime_finder(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(find_primes_fast, m)?)?;
    Ok(())
}
