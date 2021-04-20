import React, { useState } from 'react';
import axios from 'axios';
import { Icon } from "leaflet";
import { Alert, Spinner } from "react-bootstrap";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import useSWR from "swr";
import "./App.css";

export const icon = new Icon({
    iconUrl: "ship-red.png",
    shadowUrl: "ship-shadow.png",
    iconSize: [50, 50],
    iconAnchor: [0, 0],
    shadowSize: [60, 60],
    shadowAnchor: [5, 5],
    popupAnchor: [0, 0],
})

const fetcher = (url) => axios.get(url).then((res) => res.data);

const App = () => {
    const [activeShip, setActiveShip] = useState(null);

    const { data, error } = useSWR('/api/v1/ship', fetcher);
    const ships = data && !error ? data : {};
    const position = [1, 117];
    const zoom = 5;

    if (error) {
        return <Alert variant="danger">There is a problem</Alert>;
    }
    if (!data) {
        return (
            <Spinner
                animation="border"
                variant="danger"
                role="status"
                style={{
                    width: "400px",
                    height: "400px",
                    margin: "auto",
                    display: "block",
                }}
            />
        );
    }

    return (
        <MapContainer center={position} zoom={zoom}>
            <TileLayer
                attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            {ships.features.map((ship) => (
                <Marker
                    key={ship.properties.vessel_name}
                    position={[
                        ship.geometry.coordinates[1],
                        ship.geometry.coordinates[0],
                    ]}
                    onClick={() => {
                        setActiveShip(ship);
                    }}
                    icon={icon}
                    rotationAngle={30}
                    rotationOrigin="center"
                >
                    <Popup
                        position={[
                            ship.geometry.coordinates[1],
                            ship.geometry.coordinates[0],
                        ]}
                        onClose={() => {
                            setActiveShip(null);
                        }}
                    >
                        <div>
                            <h6>{ship.properties.vessel_name}</h6>
                            <p>{ship.properties.datetime}</p>
                            <p>Length (m): {ship.properties.length}</p>
                            <p>Associated: {ship.properties.status}</p>
                        </div>
                    </Popup>
                </Marker>
            ))}
        </MapContainer>
    );
};

export default App