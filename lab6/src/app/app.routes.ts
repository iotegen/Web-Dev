import { Routes } from '@angular/router';
import {HomeComponent} from "./home/home.component";
import {AboutComponent} from "./about/about.component";
import {AlbumsComponent} from "./albums/albums.component";
import {AlbumDetailComponent} from "./albums/album-detail/album-detail.component";
import {AlbumPhotosComponent} from "./albums/album-detail/album-photos/album-photos.component";
import {NgModule} from "@angular/core";


export const routes: Routes = [
  {path: '', redirectTo: 'home', pathMatch: "full"},
  {path: 'home', component: HomeComponent},
  {path: 'about', component: AboutComponent},
  {path: 'albums', component: AlbumsComponent},
  {path: 'albums/:id', component: AlbumDetailComponent},
  {path: 'photos', component: AlbumPhotosComponent}
];
