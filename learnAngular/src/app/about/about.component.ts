import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrl: './about.component.scss'
})
export class AboutComponent {

  displayedColumns: string[] = ['id', 'firstname', 'lastname', 'email', 'mobile', 'grade', 'gender'];
  dataSource: any = [];

  constructor(private http: HttpClient) { 
  console.log(this.dataSource)
  this.getStudentDetails();
}

getStudentDetails() {
  this.http.get('http://localhost:5000/student').subscribe( {
    next: (response) => {
      this.dataSource = response;
      console.log(this.dataSource)
    },
    error: (error) => {
      console.error(error)
    }  
  });
}
}


