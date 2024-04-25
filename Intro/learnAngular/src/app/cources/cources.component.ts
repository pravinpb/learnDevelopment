import { Component } from '@angular/core';

@Component({
  selector: 'app-cources',
  templateUrl: './cources.component.html',
  styleUrl: './cources.component.scss'
})
export class CourcesComponent {
  title = 'List of Cources';
  cources = ['Cource 1', 'Cource 2', 'Cource 3'];
}
