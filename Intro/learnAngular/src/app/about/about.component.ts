import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { HttpHeaders } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { SharedService } from '../shared/shared.service';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrl: './about.component.scss'
})
export class AboutComponent {
  displayedColumns: string[] = ['id', 'firstname', 'lastname', 'email', 'mobile', 'grade', 'gender', 'edit', 'delete'];
  dataSource: any = [];
  searchText: any;
  pass_message: any = [];
  delete_message: any = [];

  constructor(private http: HttpClient,private router: Router, private shared: SharedService) { 

  console.log(this.dataSource)
  this.getStudentDetails();
}

onAddNew(){
  this.router.navigate(['/contact']);
}

onEdit(element: any) {
  this.pass_message = element;
  console.log('Editing row data:', element);
  this.shared.setMessage(this.pass_message);
  this.router.navigate(['/contact']);
 }
 
onDelete(element: any) {
  const httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    }),
    responseType: 'text' as 'json'
  };
  console.log('Deleting row data:', element);
  if (confirm("Are you sure to delete this student?")){
  this.http.delete('http://localhost:5000/student/' + element['id'],httpOptions).subscribe({
    next: (response) => {
      this.getStudentDetails()
      },
      error: (error) => {
        console.error(error)
      }  
    });
  }

}

getStudentDetails() {
  this.http.get('http://localhost:5000/student').subscribe( {
    next: (response) => {
      this.dataSource = response;
      console.log("Suceess")
    },
    error: (error) => {
      console.error(error)
    }  
  });
}
}


