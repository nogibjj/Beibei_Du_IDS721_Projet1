use csv::Reader;
use csv::StringRecord;
use std::error::Error;

// The following function computes the mean of a row in the dataframe.
fn compute_mean(record: &StringRecord) -> f64 {
    let values: Vec<f64> = record
        .iter()
        // skip the first one because it indicates the country
        .skip(1)
        .map(|value| value.parse().unwrap())
        .collect();
    let sum = values.iter().sum::<f64>();
    sum / values.len() as f64
}

fn main() {
    // assign a mutable variable to read the csv file, which is for my Project 1 and this also serves as a progress bar
    let mut rdr = Reader::from_path("data/avg_wage.csv").unwrap();
    // loop through each record/row in the dataframe
    for result in rdr.records() {
        // it unwraps the result and assigns it to row
        let row = result.unwrap();
        // prints each row
        println!("{:?}", row);
        let record = StringRecord::from(row);
        let mean = compute_mean(&record);
        println!("Mean: {}", mean);
    }
}
